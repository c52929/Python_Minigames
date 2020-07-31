# Python_Minigames
This is my first Python project. As practice of coding with Python, I try making simple minigames. In my games, you will be asked about your actions. When you are asked about something, you can quit the game with answering "end", "exit" or "quit" any time.
私にとってはじめての Python プロジェクトです。Python でコードを書く練習として、簡単なミニゲームを作っています。私のゲーム内では、次にどうするかなどをあなたに問います。あなたが何かを問われている時には、 "end" や "exit" または "quit" と答えることで、ゲームを強制終了させることができます。

Shinri Run: 
	4 players, which means you and 3 coms, run toward a goal placed 20 steps ahead from starting point.
	Each player chooses one from [1, 3, 5] as number of steps run (incidentally, coms choose numbers in a random manner), but if there are some players who choose the same number, they cannot run on that turn. 
	After repeating choosing number and running, player who reach 20 steps first will be winner.
心理ラン: あなたと3台のコンピューター、つまり4人のプレイヤーは、20歩先にあるゴールを目指して進みます。それぞれのプレイヤーは毎ターンに 1,3,5 のうちひとつを選び、その数だけ進むことができます（ちなみに、コンピューターはランダムに数を選びます）。しかし、選んだ数が誰かとかぶってしまった場合、そのターンには進むことができません。それを何度か繰り返した後、20歩に到達した最初の人が優勝です。

Janken: 
	You and com fight with showing each hand as a rock, as a piece of paper or as scissors. Rock is stronger than scissors, scissors are stronger than paper, and paper is stronger than rock. If you and com show the same, you will have one more chance to fight.
じゃんけん: コンピューターとじゃんけんをします。至って普通のじゃんけんです。

Hang Man game: 
	There is a secret word chosen from more than 10,000 words in a random manner. (Words are in hangman_wordsdata\words_data.xlsx) Hit the word with guessing letters one by one included in the word.
	You have 6 lives at first. When you miss to guess, you lose 1 life. Even if you lose all the lives, you can continue the game with answering "Y" or "Yes" for this question:"Try again?" 
	When you forget the letters you have not guessed yet, you can know them with typing "list".
	* To play this game, you need to download 2 libraries xlrd and openpyxl to your computer. Download them before playing this game. Type following code into Command prompt and press Enter key to download xlrd library: pip install xlrd
	Next, type following code into Command prompt and press Enter key to download openpyxl library to your computer: pip install openpyxl
ハングマンゲーム:	1万語以上からランダムに選ばれた秘密の英単語があります。（英単語の一覧は hangman_wordsdata\words_data.xlsx の中に入っています。）その英単語に含まれているアルファベットを一文字ずつ当てて、英単語を予想してください。はじめ、あなたはライフ(HP)が6つ与えられています。予想したアルファベットがその英単語に含まれない場合、ライフを1つ失います。すべてのライフを失った後でも、 "Try again?" という質問に対して "Y" または "Yes" と答えることで、同じ英単語に再挑戦できます。まだ予想していないアルファベットを忘れてしまった時は、 "list" と答えることによってまだ予想していないアルファベットの一覧が表示されます。
* 注意 このゲームで遊ぶため、 xlrd と openpyxl という2つのPythonライブラリをコンピューターにダウンロードする必要があります。まず、 xlrd ライブラリをダウンロードするため、コマンドプロンプトを起動して、次のように入力し、Enterキーを押してください: pip install xlrd
次に、 openpyxl ライブラリをダウンロードするため、同じようにコマンドプロンプトに次のように入力し、Enterキーを押してください: pip install openpyxl
よくわからなければ、ググればたくさん出てくるので調べてみてね
