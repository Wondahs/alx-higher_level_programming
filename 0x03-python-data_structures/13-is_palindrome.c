#include "lists.h"

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
		slow = slow->next;
	while (slow != NULL)
	{
		if (slow->n != prev->n)
			return (0);
		slow = slow->next;
		prev = prev->next;
	}
	return (1);
}
