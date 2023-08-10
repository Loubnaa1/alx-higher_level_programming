#include "lists.h"

/**
 * check_cycle - function checks if singly linked list has a cycle in it.
 * @list: pointer to the beginning of the node
 * Return: 0 if no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
  listint_t *push1, *push2;

  if (list == NULL || list->next == NULL)
    return (0);
  push1 = list;
  push2 = push1->next;

  while (push1 != NULL && push2 != NULL
	 && push2->next != NULL)
    {
      if (push1 == push2)
	return (1);
      push1 = push1->next;
      push2 = push2->next->next;
    }
  return (0);
}
