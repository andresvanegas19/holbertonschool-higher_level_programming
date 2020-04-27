#include "lists.h"

/**
 * scheck_cycle - checks if a singly linked list has a cycle in it.
 * @list: is the list how it find the cycle
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	if (list == NULL)
		return(0);

	while (list != NULL)
	{
		if (list->n == list->next->next->n)
			return (1);
		list = list->next;
	}

	return (0);
}
