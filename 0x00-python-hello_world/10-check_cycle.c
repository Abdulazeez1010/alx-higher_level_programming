#include "lists.h"

/**
 */
int check_cycle(listint_t *list)
{
	listint_t *ptr;
	if (list == NULL)
		return (0);
	if (list->next == NULL)
		return (0);
	if (list->next == list)
		return (1);

	ptr = list;
	while (ptr->next != NULL)
	{
		ptr = ptr->next;
		if (ptr == list)
			return (1);
	}
	return (0);
}
