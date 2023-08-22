#include "lists.h"

/**
 * check_cycle - The function  checks if a singly linked list has a cycle in it
 * @list : The list pointer
 * Return: Returns 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *ptr, *ptr2;

	if (list == NULL)
		return (0);

	ptr = list;
	ptr2 = list;
	while (ptr != NULL && ptr->next != NULL)
	{
		ptr2 = ptr2->next;
		ptr = ptr->next->next;
		if (ptr2 == ptr)
			return (1);
	}
	return (0);
}
