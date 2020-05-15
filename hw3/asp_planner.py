#!python

from planning import PlanningProblem, Action, Expr, expr, associate;
import planning

import sys, os
import argparse
from codetiming import Timer

from asp_planner_core import solve_planning_problem_using_ASP

### Main
def main():
    # Take command line arguments
    parser = argparse.ArgumentParser();
    # parser.add_argument("input", help="Input file");
    parser.add_argument("-i", "--input", required=True, help="input file")
    parser.add_argument("-v", "--verbose", help="verbose mode", action="store_true")
    args = parser.parse_args(map(lambda x: x.lower(),sys.argv[1:]));

    input = args.input;
    verbose = args.verbose;

    # Read sudoku from input file
    if verbose:
        print("Reading planning problem and bound on plan length from " + input + "..");
    planning_problem, t_max = read_problem_from_file(input);
    if planning_problem == None:
        print("Exiting..");
        return;

    # Print information, in verbose mode
    if verbose:
        print("Planning problem:");
        print(pretty_repr_planning_problem(planning_problem));
        print("Upper bound on plan length: {}".format(t_max));

    # Solve the planning problem
    plan = None;
    timer = Timer(name="solving-time", text="Did ASP encoding & solving in {:.2f} seconds");
    if verbose:
        print("Solving planning problem using ASP encoding..");
        timer.start();
    with suppress_stdout_stderr():
        plan = solve_planning_problem_using_ASP(planning_problem,t_max);
    if verbose:
        timer.stop();

    # Print the solved sudoku
    if plan == None:
        print("NO PLAN FOUND");
    else:
        if verify_plan(planning_problem,plan) == True:
            if verbose:
                print("Correct plan found:");
            print(pretty_repr_plan(plan));
        else:
            print("INCORRECT PLAN FOUND");
            print(pretty_repr_plan(plan));


### Read planning problem from file
def read_problem_from_file(filename):

    # Auxiliary function to parse a string of the form (prefix + "rest")
    # If string is of this form, it returns True,"rest"
    # Otherwise, it returns False,""
    def remove_prefix_if_possible(line, prefix):
        if line[0:len(prefix)] == prefix:
            return True,line[len(prefix):];
        else:
            return False,"";

    try:
        file = open(filename, "r");
        # Initialize
        initial_str = "";
        goals_str = "";
        t_max_str = "20"; # default value is 20
        actions_list = [];
        # Read the file line by line
        for line in file.readlines():
            stripped_line = line.strip();
            if stripped_line != "" and stripped_line[0] != '#':
                # Lines specifying initial state
                match,rest_of_line = remove_prefix_if_possible(stripped_line,"initial: ");
                if match:
                    initial_str = rest_of_line.strip();
                    if expr(initial_str) == True or expr(initial_str) == None:
                        initial_str = "[]";
                # Lines specifying goals
                match,rest_of_line = remove_prefix_if_possible(stripped_line,"goals: ");
                if match:
                    goals_str = rest_of_line.strip();
                    if expr(goals_str) == True or expr(goals_str) == None:
                        goals_str = "[]";
                # Lines specifying t_max
                match,rest_of_line = remove_prefix_if_possible(stripped_line,"t_max: ");
                if match:
                    t_max_str = rest_of_line.strip();
                # Lines specifying an action
                match,rest_of_line = remove_prefix_if_possible(stripped_line,"action: ");
                if match:
                    action_strs = rest_of_line.split(";");
                    action = Action(action_strs[0], precond=action_strs[1], effect=action_strs[2]);
                    if expr(action.precond) == None or expr(action.precond) == True:
                        action.precond = [];
                    if expr(action.effect) == None or expr(action.effect) == True:
                        action.effect = [];
                    actions_list.append(action);
        # Create planning_problem and t_max from the data stored after reading, and return them
        planning_problem = PlanningProblem(initial=initial_str, goals=goals_str, actions=actions_list);
        t_max = int(t_max_str);
        return planning_problem, t_max;

    # If exception occurs, print error message and return None,None
    except Exception as e:
        print("Something went wrong while reading from " + filename + " (" + str(e) + ")");
        return None, None;

### Verify whether a plan is correct for a planning problem
def verify_plan(planning_problem, plan):

    # Make a copy of the problem
    copy = copy_planning_problem(planning_problem);
    # Execute the actions on the copy
    try:
        for action in plan:
            copy.act(expr(action));
    except:
        # If something goes wrong, it is not a correct plan
        return False;
    # Return whether the goal is satisfied
    return copy.goal_test();


### String representation of plans
def pretty_repr_plan(plan):
    return str(plan);


### Make a copy of a planning problem
def copy_planning_problem(planning_problem):
    copy = PlanningProblem(
        initial=planning_problem.initial,
        goals=planning_problem.goals,
        actions=planning_problem.actions);
    return copy;


### Pretty (human-readable) string representation of planning problems
def pretty_repr_planning_problem(planning_problem):

    repr = "--- Planning problem ---\n";
    repr += "Initial: {}\n".format(planning_problem.initial);
    repr += "Goals: {}\n".format(planning_problem.goals);
    repr += "Actions: \n";
    for action in planning_problem.actions:
        repr += "  * {}\n".format(Expr(action.name, *action.args));
        repr += "    precondition: {}\n".format(action.precond);
        repr += "    effect: {}\n".format(action.effect);
    repr += "---";
    return repr;


### Write a planning problem to a file in the same format that is read by read_problem_from_file()
def write_planning_problem_to_file(planning_problem,t_max,filename):

    output = "# Initial state\n";
    output += "initial: {}\n".format(associate('&', planning_problem.initial));
    output += "# Goals\n";
    output += "goals: {}\n".format(associate('&', planning_problem.goals));
    for action in planning_problem.actions:
        output += "# Action {}\n".format(action);
        precond_str = "True";
        if action.precond != None and action.precond != True:
            precond_str = associate('&', action.precond);
        effect_str = "True";
        if action.effect != None and action.effect != True:
            effect_str = associate('&', action.effect);
        output += "action: {}; {}; {}\n".format(
            str(action),
            precond_str,
            effect_str
        );
    output += "# T_max\n";
    output += "t_max: {}".format(t_max);

    try:
        file = open(filename, "w");
        file.write(output);
        file.close();

    except Exception as e:
        print("Something went wrong while writing to " + filename + " (" + str(e) + ")");


###
class suppress_stdout_stderr(object):
    '''
    A context manager for doing a "deep suppression" of stdout and stderr in
    Python, i.e. will suppress all print, even if the print originates in a
    compiled C/Fortran sub-function.
       This will not suppress raised exceptions, since exceptions are printed
    to stderr just before a script exits, and after the context manager has
    exited (at least, I think that is why it lets exceptions through).

    (From: https://stackoverflow.com/questions/11130156/suppress-stdout-stderr-print-from-python-functions)
    '''
    def __init__(self):
        # Open a pair of null files
        self.null_fds =  [os.open(os.devnull,os.O_RDWR) for x in range(2)]
        # Save the actual stdout (1) and stderr (2) file descriptors.
        self.save_fds = (os.dup(1), os.dup(2))

    def __enter__(self):
        # Assign the null pointers to stdout and stderr.
        os.dup2(self.null_fds[0],1)
        os.dup2(self.null_fds[1],2)

    def __exit__(self, *_):
        # Re-assign the real stdout/stderr back to (1) and (2)
        os.dup2(self.save_fds[0],1)
        os.dup2(self.save_fds[1],2)
        # Close the null files
        os.close(self.null_fds[0])
        os.close(self.null_fds[1])


### Call main()
if __name__ == "__main__":
    main();
