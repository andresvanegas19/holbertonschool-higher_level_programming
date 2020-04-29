#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: pointer to head of list
 * @number: is the new data in the new node
 *
 * Return: the address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *pHead, *newNode;

	if (number <= 0 || !(*head))
	{
		newNode = insert_begging(head, number);
		return (newNode);
	}

	pHead = *head;
	newNode = malloc(sizeof(listint_t));
	if (newNode == NULL)
		return (NULL);
	newNode->n = number;
	newNode->next = NULL;

	while (pHead)
	{
		if ((!(pHead->next) || number <= pHead->next->n) || number <= pHead->n)
		{
			if (pHead->next == NULL)
			{
				pHead->next = newNode;
				return (newNode);
			}
			newNode->next = pHead->next;
			pHead->next = newNode;
			return (newNode);
		}
		pHead = pHead->next;
	}
	return (NULL);
}

/**
 * insert_begging - inserts a number into a sorted singly linked list.
 * @head: pointer to head of list
 * @number: is the new data in the new node
 *
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_begging(listint_t **head, int number)
{
	listint_t *newNode;

	newNode = malloc(sizeof(listint_t));
	if (newNode == NULL)
		return (NULL);

	newNode->next = *head;
	newNode->n = number;
	*head = newNode;

	return (newNode);
}
