#include "lists.h"

/**
 * check_cycle - this is a C function that checks if a
 * singly linked list has a cycle in it
 * @list: the linked lisk to be checked
 * Return: 0 if there is nocycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *fst = list;
	listint_t *slw = list;

	if (!list)
		return (0);
	while (slw && fst && fst->next)
	{
		slw = slw->next;
		fst = fst=>next->next;
		if (fst == slw)
			return (1);
	}
	return (0);
}
