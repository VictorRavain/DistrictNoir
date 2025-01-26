# District Noir
Dans les plus grandes organisations criminelles de la ville, des hommes et des femmes s'affrontent pour faire grandir leur influence. Le contrôle du District Noir, une zone très contestée, est un enjeu majeur et primordial pour dominer la ville.

Dans District Noir vous devez avoir, à l'issue des 4 manches, plus de points que votre adversaire en récupérant une majorité de cartes Soutiens. Vous pouvez également l'emporter immédiatement en contrôlant les trois cartes Ville (qui représentent les lieux stratégiques de la ville).

## MISE EN PLACE
Mélangez les 45 cartes du jeu. Retirez ensuite 3 cartes sans les regarder et placez-les dans la boîte de jeu. Elles ne seront pas utilisées pendant cette partie. Distribuez 5 cartes face cachée à chaque joueur. Ces cartes constituent votre main de départ Piochez 2 cartes de la pioche et placez-les face visible au centre de la table en composant une ligne depuis la pioche. Lancer le jeton qui determinera qui commencera la première manche, ensuite les joueurs alternent.

## DÉROULEMENT DE LA PARTIE
Une partie se déroule en 4 manches. À chaque manche, en commençant par la première joueur et à tour de rôle, les joueurs vont effectuer une action parmi deux possibles :
- JOUER une carte au bout de la ligne 
- Dans la ligne, PRENDRE les 5 dernières cartes jouées (1 seule fois par manche). Les joueurs jouent à tour de rôle 6 fois chacune.

### JOUER UNE CARTE
Le joueur choisit une carte de sa main et la pose au bout de la ligne. Si sa main est vide, le joueur ne peut plus choisir cette action et doit choisir la deuxième action pour prendre des cartes au centre de la table.

### PRENDRE DES CARTES :
En commençant par la dernière carte de la ligne, le joueur doit prendre exactement 5 cartes, et les poser devant elle, en les classant selon leur type (SOUTIEN, ALLIANCE, TRAHISON et VILLE). II est impossible de choisir cette action si aucune carte n'est disponible dans la ligne. II est cependant possible d'effectuer cette action si moins de 5 cartes sont disponibles. Dans ce dernier cas, le joueur prend l'ensemble des cartes de la ligne et les pose devant elle.

Remarque : les cartes récupérées et posées devant chaque joueur sont gardées jusqu'à la fin de la partie.

### Important : 
les joueurs ne peuvent effectuer l'action PRENDRE DES CARTES qu'une seule fois par manche. Dès qu'un joueur a effectué cette action, s'il lui reste des cartes en main, elle devra désormais effectuer l'action JOUER UNE CARTE lors de ses prochains tours, et cejusqu'à la fin de la manche. Chaque joueur effectuera donc, dans chaque manche, 5 fois l'action JOUER UNE CARTE et 1 seule fois l'action PRENDRE DES CARTES.

## FIN DE LA MANCHE
Une manche se termine lorsque les deux joueuses ont effectué 6 actions, les mains des 2 joueuses sont alors vides. Une fois la manche terminée, si la pioche est vide la partie est terminée et chaque joueuse établit son score pour déterminer qui l'emporte. S'il reste des cartes dans la pioche, les joueuses piochent 5 cartes chacune pour refaire leur main et une nouvelle manche commence. Le jeton CAMP est donné à l'autre joueuse qui le retourne sur la face symbolisant son CAMP.

Remarque : il est tout à fait possible qu'en fin de manche, des cartes soient encore présentes dans la ligne. Elles sont laissées dans la ligne pour la manche suivante.

### Important : 
si, durant n'importe laquelle des manches, une joueuse parvient à rassembler les 3 cartes VILLE, la partie s'arrête immédiatement et cette joueuse remporte la partie sans que les scores ne soient calculés.

## FIN DE LA PARTIE
La partie s'arrête quand les joueuses ont joué 4 manches (la pioche est alors vide). Le calcul des scores se fait comme suit :
- Pour chaque type de SOUTIEN, la joueuse qui a la majorité marque un nombre de points égal au chiffre représenté sur ce SOUTIEN.
- En cas d'égalité sur un type de SOUTIEN, aucune des deux joueuses ne gagne les points de victoire correspondants.
- Chaque série de 4 SOUTIENS différents rapporte 5 points de victoire supplémentaires à sa propriétaire. 
- A ces points de victoire, les joueuses ajoutent et/ou retirent les points figurant sur leurs cartes ALLIANCE et TRAHISON.

La joueuse qui a le total de points de victoire le plus élevé emporte la partie. En cas d'égalité, la joueuse qui l'emporte est celle qui remporte la majorité des cartes SOUTIEN de valeur 8, puis en cas de nouvelle égalité la majorité des cartes SOUTIEN de valeur 7, etc. 

Remarque : les cartes VILLE ne valent aucun point de victoire lors du calcul du score final.

## CARTES SOUTIEN
Ces cartes représentent les grands groupes d'influence dans le District Noir. Chaque SOUTIEN possède un nombre de membres défini et il s'agira d'en obtenir le plus possible pour avoir une chance de l'emporter.

## CARTES VILLE
Ces 3 cartes représentent les 3 lieux stratégiques de la VILLE les docks, le commissariat et la mairie. À tout moment, si vous parvenez à obtenir ces 3 cartes, vous remportez immédiatement la partie !

## CARTES ALLIANCE ET TRAHISON
Ces cartes représentent les accords ou les traîtrises qui jalonnent votre parcours vers le contrôle du District Noir. À vous de tout faire pour récupérer les bonnes cartes et éviter les mauvaises !

## JETON CAMP
Ce jeton symbolise les deux camps qu'il est possible d'incarner dans le jeu. Chaque joueur choisira un des deux camps en début de partie et ce jeton sera utilisé pour déterminer quelle joueur joue en premier à chaque début de manche.

## Matériel
47 cartes  réparties comme suit : 26 cartes SOUTIEN (5 de valeur 5, 6 de valeur 6, 7 de valeur 7 et 8 de valeur 8) - 7 cartes ALLIANCE - 9 cartes TRAHISON - 3 cartes VILLE, 1 jeton CAMP (recto-verso).

# Code
First step : 
I created a virtual env with ``python -m venv venv``
activated it : ``venv\Scripts\activate``

To save the dependencies : ``pip freeze > requirements.txt``

To install requirements : ``pip install -r requirements.txt``