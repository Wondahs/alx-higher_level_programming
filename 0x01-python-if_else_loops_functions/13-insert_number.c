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
	listint_t *newNode, *current;

	newNode = (listint_t *)malloc(sizeof(listint_t));
	if (!newNode || !head)
		return (NULL);
	current = *head;
	newNode->n = number;
	while (current != NULL)
	{
		if (current->next->n > number)
			break;
		current = current->next;
	}
	newNode->next = current->next;
	current->next = newNode;

	return (*head);
}
