// DO NOT REMOVE THIS COMMENT!! CSE 3430 lab2.c AU 24 CODE 052108

// STUDENT NAME: Syan Raval

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

	struct Data {
		char title[55];
		char author[55];
		int stockNumber;
		float wholesalePrice;
		float retailPrice;
		int wholesaleQuantity;
		int retailQuantity;
	};

	typedef struct Node {
		struct Data book;
		struct Node *next;
	} Node;

void getDataAndBuildList(Node **listHeadPtr);
Node *createNodeAndGetData(void);
void insertNode(Node **listHeadPtr, Node *newNodePtr);
void deleteNode(Node **listHeadPtr, int stockNumToDelete);
void getUserOption(Node **listHead);
double calculateTotalRevenue(const Node *listHead);
double calculateInvestmentInInventory(const Node *listHead);
double calculateTotalWholesaleCost(const Node *listHead);
double calculateTotalProfit(const Node *listHead);
int calculateTotalBooksSold(const Node *listHead);
double calculateAverageProfit(const Node *listHead);
void printList(const Node *listHead);
void freeAllNodes(Node **listHeadPtr);

int main() {
	Node *listHead = NULL;
	getDataAndBuildList(&listHead);
	getUserOption(&listHead);
	return 0;
}

void getDataAndBuildList(Node **listHeadPtr) {
	Node *newNodePtr;
	printf("Please enter data about the books.\n\n");
	while (newNodePtr = createNodeAndGetData()) {
		insertNode(listHeadPtr, newNodePtr);
	}
}

Node *createNodeAndGetData(void) {
	Node *newNodePtr;
	newNodePtr = malloc (sizeof(Node));
	if (newNodePtr == NULL) {
		printf("Error: memory could not be allocated for enough nodes. ");
		printf("Terminating program!\n");
		exit (0);
	}
	else {
		scanf("%[^\n]", newNodePtr->book.title);
		if (strcmp(newNodePtr->book.title, "END_DATA") == 0) {
			/* free Node if end of book data detected */
			free(newNodePtr);			
			return NULL;
		}
		else {
			/* consume newline before author string */
			getchar();
			scanf("%[^\n]s", newNodePtr->book.author);
			scanf("%i", &newNodePtr->book.stockNumber);
			scanf("%f", &newNodePtr->book.wholesalePrice);
			scanf("%f", &newNodePtr->book.retailPrice);
			scanf("%i", &newNodePtr->book.wholesaleQuantity);
			scanf("%i", &newNodePtr->book.retailQuantity);
			/* consume newline before next title string */
			getchar();				
		}
		return newNodePtr;
	}
}


void insertNode(Node **listHeadPtr, Node *newNodePtr) {
	
	Node *traversePtr = *listHeadPtr;
	
    // Add the first Node to an empty list 
    if (traversePtr == NULL) { 
        *listHeadPtr = newNodePtr; 
        newNodePtr->next = NULL; 
    } 
    
    // Add a Node as the first Node in a non-empty list 
    else if (newNodePtr->book.stockNumber < traversePtr->book.stockNumber) { 
        *listHeadPtr = newNodePtr; 
        newNodePtr->next = traversePtr; 
    }
    
    // Add a new Node to a non-list after the current first Node 
    else { 
        Node *priorNodePtr = traversePtr; 
        traversePtr = traversePtr->next;  
        while (traversePtr != NULL && traversePtr->book.stockNumber < newNodePtr->book.stockNumber) { 
            priorNodePtr = traversePtr; 
            traversePtr = traversePtr->next; 
        } 
        priorNodePtr->next = newNodePtr; 
        newNodePtr->next = traversePtr; 
    }
}

void getUserOption(Node **listHeadPtr) {
	int option;
	Node *newNodePtr;
	int stockNumToDelete;
	do {
		printf("\nPlease enter an integer between 1 and 10 to select an operation on the data:\n");
		scanf("%i", &option);
		getchar();
		switch (option){
			case 1:
				printList (*listHeadPtr);
				break;
			case 2:
				printf("\nTotal revenue: %.2f\n", calculateTotalRevenue(*listHeadPtr));
				break;
			case 3:
				printf("\nTotal wholesale cost: %.2f\n", calculateTotalWholesaleCost(*listHeadPtr));
				break;
			case 4:
				printf("\nTotal investment in inventory: %.2f\n", calculateInvestmentInInventory(*listHeadPtr));
				break;
			case 5:
				printf("\nTotal profit: %.2f\n", calculateTotalProfit(*listHeadPtr)); 
				break;
			case 6:
				printf("\nTotal number of books sold = %i\n", calculateTotalBooksSold(*listHeadPtr));
				break;
			case 7:
				printf("\nAverage profit: %.2f\n", calculateAverageProfit(*listHeadPtr));
				break;
			case 8:		
				printf("\nPlease enter the data for the book you wish to add:\n\n");
				newNodePtr = createNodeAndGetData();
				insertNode(listHeadPtr, newNodePtr);			
				break;
			case 9:
				printf("\nEnter the stock number of the book you wish to delete: ");
				scanf("%i", &stockNumToDelete);
				deleteNode(listHeadPtr, stockNumToDelete);
				break;
			case 10:
				freeAllNodes(listHeadPtr);
				break;
			default:
				printf("Valid option choices are 1 to 10. Please choose again!\n");
				break;
		} 
	} while (option != 10);
}

double calculateTotalRevenue(const Node *listHead) {
    
	float rev_sum = 0;
    const Node *traversePtr = listHead;
        while (traversePtr != NULL) {		/* determine not at end of list */

		    rev_sum += traversePtr->book.retailPrice * traversePtr->book.retailQuantity;

		    traversePtr = traversePtr->next;
	     }
	return rev_sum;
	
}

double calculateInvestmentInInventory(const Node *listHead) {
    
    float inventory = 0;
    const Node *traversePtr = listHead;
        while (traversePtr != NULL) {		/* determine not at end of list */
    
    		inventory += (traversePtr->book.wholesaleQuantity - traversePtr->book.retailQuantity)
    		* traversePtr->book.wholesalePrice;
    		    
    		traversePtr = traversePtr->next;
        }
    return inventory;
    	
}

double calculateTotalWholesaleCost(const Node *listHead) { 

    float whole_sum= 0;
    const Node *traversePtr = listHead;
	     while (traversePtr != NULL) {		/* determine not at end of list */
		    whole_sum += traversePtr->book.wholesalePrice *
		    traversePtr->book.wholesaleQuantity;
		    traversePtr = traversePtr->next;
	    }
	return whole_sum;

}

double calculateTotalProfit(const Node *listHead) { 
	
    return calculateTotalRevenue(listHead) -
    calculateTotalWholesaleCost(listHead) +
    calculateInvestmentInInventory(listHead);

}

int calculateTotalBooksSold(const Node *listHead) { 

    int ret_sum = 0;
    const Node *traversePtr = listHead;
	     while (traversePtr != NULL) {		/* determine not at end of list */
		    ret_sum += traversePtr->book.retailQuantity;
		    traversePtr = traversePtr->next;
	    }
	return ret_sum;

}

double calculateAverageProfit(const Node *listHead) {

    return calculateTotalProfit(listHead) /
    calculateTotalBooksSold(listHead);

}

void deleteNode(Node **listHeadPtr, int stockNumToDelete) {

	Node *traversePtr = *listHeadPtr;
	
    // Three cases, similar to insertNode 
    // First case – delete first Node from empty list
    
    if (traversePtr == NULL) { 
        printf ("ERROR; List is empty, so cannot delete!\n"); 
    }
    
    // Second case – delete first Node in non-empty list 
    else if (traversePtr->book.stockNumber == stockNumToDelete) { 
        *listHeadPtr = traversePtr->next; 
        free (traversePtr); 
    }
    
    // Third case – delete Node after first Node in non-empty list 
    else { 
        Node *priorNodePtr = traversePtr; 
        traversePtr = traversePtr->next; 
        while (traversePtr != NULL &&  traversePtr->book.stockNumber != stockNumToDelete) { 
            priorNodePtr = traversePtr; 
            traversePtr = traversePtr->next; 
        } 
        if (traversePtr == NULL || traversePtr->book.stockNumber != stockNumToDelete) { 
            printf ("ERROR: Book stock number %i is not in the list!\n", stockNumToDelete); 
        } 
    else { 
        priorNodePtr->next = traversePtr->next; 
        free (traversePtr); 
        }
    }	
}

void printList(const Node *listHead) {
	const Node *traversePtr = listHead;
	printf("\nBook list:\n");
	while (traversePtr != NULL) {		/* determine not at end of list */
		printf("%s\n", traversePtr->book.title); 
		traversePtr = traversePtr->next;
	}
	printf("\n");
}

void freeAllNodes(Node **listHeadPtr) {
	Node *traversePtr = *listHeadPtr;
	Node *restOfListPtr = *listHeadPtr;    
	while (restOfListPtr != NULL) {         /* determine list is not empty */
		restOfListPtr = restOfListPtr->next;
		free(traversePtr);
		traversePtr = restOfListPtr;
	}
	*listHeadPtr = NULL; /* set listHeadPtr back to NULL after space freed */
}
