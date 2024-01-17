#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly linked list
 * @head: Double pointer to a singly linked list
 * @number: Value of the new node
 * Return: The address of the new node, or NULL if it failed.
 */

listint_t *insert_node(listint_t **head, int number)
{
	int flag = 0;
	listint_t *n_node = NULL, *node_x = NULL, *xr = NULL;
	
	if (head == NULL)
		return (NULL);
	n_node = malloc(sizeof(listint_t));
	if (!n_node)
		return (NULL);
	n_node->n = number, n_node->next = NULL;
	if (*head == NULL)
	{
		*head = n_node;
		return (*head);
	}
	node_x = *head;
	if (number <= node_x->n)
	{
		n_node->next = node_x, *head = n_node;
		return (*head);
	}
	if (number > node_x->n && !node_x->next)
	{
		node_x->next = n_node;
		return (n_node);
	}
	xr = node_x->next;
	while (node_x)
	{
		if (!xr)
			node_x->next = n_node, flag = 1;
		else if (xr->n == number)
			node_x->next = n_node, n_node->next = xr, flag = 1;
		else if (xr->n > number && node_x->n < number)
			node_x->next = n_node, n_node->next = xr, flag = 1;
		if (flag)
			break;
		xr = xr->next, node_x = node_x->next;
	}
	return (n_node);
}
