#include "lists.h"
/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer 
 * @number: number to insert
 * Return: pointer to the new node or NUll if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *temp;
	

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;

	while (stock != NULL)
	{
		if (new->n > stock->n)
		{
			temp = stock;
			stock = stock->next;
		}
		else
		{
			new->next = stock;
			temp->next = new;
			return (new);
		}
	}
	return (NULL);
}
