#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: pointer to head of list
 * Return: number of nodes
 */
int is_palindrome(listint_t **head)
{
    listint_t *copyHead = *head, *pHead = *head;
    dlistint_t *headdouble, *tail;
    int palindromo = 0, size = 0;

    if (*head == NULL)
        return (1);

    headdouble = NULL;
    while (copyHead)
    {
        tail = add_dnodeint(&headdouble, copyHead->n);
        copyHead = copyHead->next;
        size++;
    }
    while (pHead && tail)
    {
        if (pHead->n == tail->n)
            palindromo++;
        pHead = pHead->next;
        tail = tail->prev;
    }
    if (size == palindromo)
    {
        free_dlistint(headdouble);
        return (1);
    }

    free_dlistint(headdouble);
    return (0);
}

/**
 * add_dnodeint - adds a new node at the beginning of a dlistint_t list.
 * @head: is the double linked list
 * @n: is the content of the node
 *
 * Return: the address of the new element, or NULL if it failed
 */
dlistint_t *add_dnodeint(dlistint_t **head, const int n)
{
	dlistint_t *newNode = *head;

	newNode = malloc(sizeof(dlistint_t));
	if (newNode == NULL)
		return (NULL);

	newNode->next = NULL, newNode->prev = NULL;
	newNode->n = n;

	if (*head == NULL)
	{
		*head = newNode;
		return (*head);
	}

	newNode->next = *head;
	*head = newNode;
	newNode->next->prev = newNode;

	return (newNode);
}



/**
 * free_dlistint -  free a dlistint_t list avoid leaks.
 * @head: point to the double linked list
 *
 */
void free_dlistint(dlistint_t *head)
{
	dlistint_t *pHead = head;

	while (head)
	{
		pHead = head->next;
		free(head);
		head = pHead;
	}
}
