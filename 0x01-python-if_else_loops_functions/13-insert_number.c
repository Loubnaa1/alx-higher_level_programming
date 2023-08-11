#include "lists.h"
/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer 
 * @number: number to enter
 * Return: pointer to the new node or NUll if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
  listint_t *alt, *neu, *s;

  s = *head;
  if (head == NULL)
    return (NULL);

  neu = malloc(sizeof(listint_t));
  if (neu == NULL)
    return (NULL);

  neu->n = number;
  neu->next = NULL;

  while (s != NULL)
	{
		if (neu->n < s->n)
		{
			neu->next = s;
                        alt->next = neu;
 			return (neu);
		}
		else
		{
			alt = s;
                        s = s->next;
		}
	}
  
  return (neu);
}
