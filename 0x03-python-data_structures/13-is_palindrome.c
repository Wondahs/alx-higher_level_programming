#include "lists.h"
#include <unistd.h>

int check_size(listint_t **head);
listint_t *reverse_list(listint_t **head);

/**
 *reverse_list - Reverses a linked list
 *@head: Pointer to a pointer to the head of a linked list
 *
 * Return: Reversed list
 */
listint_t *reverse_list(listint_t **head)
{
	listint_t *current, *previous, *next;

	if (!*head || *head == NULL)
		return (NULL);
	current = *head;
	previous = NULL;
	while (current)
	{
		next = current->next;
		current->next = previous;
		previous = current;
		current = next;
	}
	*head = previous;
	return (*head);
}
/**
 *check_size - Checks the size of a listint_t linked list
 *@head: Pointer to a pointer to the head of a linked list
 *
 *Return: Size of linked list.
 */
int check_size(listint_t **head)
{
	listint_t *start = *head;
	int size = 0;

	if (start == NULL)
		return (0);

	while (start != NULL)
	{
		size++;
		start = start->next;
	}

	return (size);
}

/**
 * is_palindrome - Checks if a linked list of integers is a palindrome.
 * @head: Pointer to a pointer to the head of the linked list.
 *
 * Return: 1 if the linked list is a palindrome, 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
	listint_t *start, *left, *right, *mid;
	int size, i;

	if (!*head)
		return (0);

	if (*head == NULL)
		return (1);

	start = *head;
	right = *head;
	size = check_size(&start);
	for (i = 0; i < size / 2; i++)
	{
		start = start->next;
	}
	if (size % 2 == 0)
		left = start;
	else
		left = start->next;
	left = reverse_list(&right);
	mid = right;

	while (right)
	{
		if (right->n != left->n)
			return (0);
		right = right->next;
		left = left->next;
	}
	reverse_list(&mid);

	return (1);
}
