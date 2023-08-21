#include "lists.h"

/**
 */
int check_cycle(listint_t *list)
{
	listint_t *ptr;

	ptr = list;
	while (ptr->next != NULL)
	{
		ptr = ptr->next;
		if (ptr == list)
			return (1);
	}
	return (0);
}
