#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>
/**
* infinite_while - infinite_while
* Return: exit status
*/
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
/**
* main - main
* Return: exit code
*/
int main(void)
{
	int i = 0;

	for (i = 0; i < 5; i++)
	{
		pid_t child_pid = fork();

		if (child_pid > 0)
		{
			printf("Zombie process created, PID: %d\n", child_pid);
			sleep(1);
		}
		else
		{
			exit(0);
		}
	}
	return (infinite_while());
}
