#include "lists.h"

/**
 * insert_node - The function inserts a number into a sorted singly linked list
 * @head : The head pointer
 * @number : The number to insert
 * Return: Returns the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *ptr, *ptr2, *temp;

	if (*head == NULL)
		return (NULL);
	temp = malloc(sizeof(listint_t));
	if (temp == NULL)
		return (NULL);
	temp->n = number;
	temp->next = NULL;

	if ((*head)->n > number)
	{
		temp->next = *head;
		*head = temp;
		return (temp);
	}

	ptr = *head;
	while (ptr != NULL && ptr->n < number)
	{
		ptr2 = ptr;
		ptr = ptr->next;
	}
	ptr2->next = temp;
	temp->next = ptr;
	return (temp);
}
