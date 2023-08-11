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

  if (head == NULL)
    return (NULL);

  neu = malloc(sizeof(listint_t));
  if (neu == NULL)
    return (NULL);

  neu->n = number;
  s = *head;
  neu->next = NULL;
  for (; s != NULL && neu->n > s->n;)
    {
      alt = s;
      s->next = neu;
    }
  if (neu->n < s->n)
    {
      neu->next = s;
      alt->next = neu;
      return (neu);
    }
  
  return (new);
}
