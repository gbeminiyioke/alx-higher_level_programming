#include "lists.h"

listint_t *rev_listint(listint_t **head);
int is_palindrome(listint_t **head);

/**
 * rev_listint - Reverses a singly-linked
 * listint_t list.
 * @head: A pointer to the starting node of the
 * list to reverse.
 * Return: A pointer to the head of the reversed list
 */

listint_t *rev_listint(listint_t **head)
{
	listint_t *node = *head;
	listint_t *prev = NULL;
	listint_t *next;

	while (node)
	{
		next = node->next;
		node->next = prev;
		prev = node;
		node = next;
	}
	*head = prev;
	return (*head);
}

/**
 * is_palindrome - Checks if a singly linked list
 * is a palindrome.
 * @head: A pointer to the head of the linked list.
 * Return: If the linked list is not a palindrome - 0.
 * If the linked list is a palindrome - 1.
 */
int is_palindrome(listint_t **head)
{
	listint_t *new;
	listint_t *rvs;
	listint_t *mid;
	size_t itm;
	size_t itm_sz = 0;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	new = *head;
	while (new)
	{
		itm_sz++;
		new = new->next;
	}

	new = *head;
	for (itm = 0; itm < (itm_sz / 2) - 1; itm++)
		new = new->next;

	if ((itm_sz % 2) == 0 && new->n != new->next->n)
		return (0);

	new = new->next->next;
	rvs = rev_listint(&new);
	mid = rvs;

	new = *head;
	while (rvs)
	{
		if (new->n != rvs->n)
			return (0);
		new = new->next;
		rvs = rvs->next;
	}
	rev_listint(&mid);

	return (1);
}
