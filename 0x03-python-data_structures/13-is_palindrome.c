#include "lists.h"
#include <unistd.h>

/**
 * link_lists - Links list @mid to @head
 * @head: List 1
 * @mid: List 2
 *
 * Return: Linked list.
 */
listint_t *link_lists(listint_t **head, listint_t **mid)
{
	listint_t *start = *head;

	while (start->next != NULL)
		start = start->next;
	start->next = *mid;

	return (*head);
}

/**
 * reverse_list - Reverses a linked list
 * @head: Pointer to a pointer to the head of a linked list
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
 * is_palindrome - Checks if a linked list of integers is a palindrome.
 * @head: Pointer to a pointer to the head of the linked list.
 *
 * Return: 1 if the linked list is a palindrome, 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
	listint_t *fast, *slow, *prev, *tmp, *rev;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	fast = *head;
	slow = *head;
	prev = NULL;

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		tmp = slow;
		slow = slow->next;
		tmp->next = prev;
		prev = tmp;
	}
	if (fast != NULL)
	{
		tmp = slow;
		slow = slow->next;
	}
	else
		tmp = slow;
	rev = prev;
	while (slow != NULL)
	{
		if (slow->n != prev->n)
		{
			reverse_list(&rev);
			link_lists(&rev, &tmp);
			return (0);
		}
		slow = slow->next;
		prev = prev->next;
	}
	reverse_list(&rev);
	link_lists(&rev, &tmp);
	return (1);
}
