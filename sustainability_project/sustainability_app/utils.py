# utils.py - Helper functions for sustainability_app

def add_action(actions_list, action):
    """Add a new action to the list."""
    actions_list.append(action)
    return actions_list

def get_actions(actions_list):
    """Retrieve all actions."""
    return actions_list

def delete_action(actions_list, action):
    """Remove an action from the list."""
    if action in actions_list:
        actions_list.remove(action)
    return actions_list
