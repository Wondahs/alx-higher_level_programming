#include "lists.h"

/**
 *check_cycle - Checks if a listint_t list has a cycle
 *@list: List to check
 *
 *
 *Return: 0 if no cycle, 1 if cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *tortoise = list;
	listint_t *hare = list->next;

	if (!list)
		return (0);

	while (tortoise && hare && hare->next)
	{
		if (tortoise == hare)
			return (1);
		tortoise = tortoise->next;
		hare = hare->next->next;
	}
	return (0);
}
