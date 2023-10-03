#include "lists.h"
#include <stdlib.h>
/**
 *insert_node - Inserts node in a sorted listint_t list
 *@head: First node
 *@number: Value of new node
 *
 *Return: NULL if unsuccessful, pointer to head node if successful
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newNode, *current, *previous;

	newNode = (listint_t *)malloc(sizeof(listint_t));
	if (!newNode || !head)
		return (NULL);
	current = *head;
	previous = NULL;
	newNode->n = number;
	newNode->next = NULL;
	if (*head == NULL)
	{
		*head = newNode;
		return (*head);
	}
	while (current != NULL)
	{
		if (current->n > number)
		{
			if (previous == NULL)
				*head = newNode;
			else
				previous->next = newNode;
			newNode->next = current;
			break;
		}
		previous = current;
		current = current->next;
	}

	return (*head);
}
