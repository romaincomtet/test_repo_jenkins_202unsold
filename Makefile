##
## EPITECH PROJECT, 2019
## 110borwein_2019
## File description:
## Makefile
##

NAME	=  	202unsold

SRC		=   $(addprefix src/,		\
						202unsold.py)

all: $(NAME)

$(NAME):	
				@cp $(SRC) $(NAME) 
				@echo -e "\033[32mCopied $(SRC) into $(NAME)\033[0m"
				@chmod 755 $(NAME)
				@echo -e "\033[32mPermission granted\033[0m"
				@echo -e "\033[1m\033[31mCompilation\033[0m \033[34msuccessful\033[21m\033[0m"

clean:
				@rm $(NAME)
				@echo -e "\033[35mRm $(NAME)\033[0m"

fclean: clean
				rm $(NAME)

re: clean all

%.o: %.c
				@$(CC) $(CFLAGS) -c -o $@ $<			\
				&& echo "\e[32m[OK] \e[1m" $< "\e[0m"	\
				|| echo "\e[31m[KO] \e[1m" $< "\e[0m"% %