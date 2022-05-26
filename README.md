# KissManngaApi
An Unofficial Python API Library to Download Manga  for FREE...

## Installation
```$ pip install kissmanga```

## Usage
### 1. Importing the Library
```from kissmanga import get_search_results, get_manga_details, get_manga_episode, get_manga_chapter```
### 2. Searching manga
```manga_search = get_search_results(query="Naruto")```
###
#### Manga Search Result
```
[{'title': 'Naruto', 'mangaid': 'naruto'},
           {'title': 'Boruto: Naruto Next Generations', 'mangaid': 'boruto-naruto-next-generations'}, 
        {'title': 'Naruto - Full Color', 'mangaid': 'naruto-full-color'}, 
    {'title': 'Naruto Gaiden: The Seventh Hokage', 'mangaid': 'naruto-gaiden-the-seventh-hokage'}, 
{'title': "Naruto: Chibi Sasuke's Sharingan Legend", 'mangaid': 'naruto-chibi-sasukes-sharingan-legend'}]
```
###
#### Getting the title of manga search results:
```
for k in manga_search:
    print(k.get('title'))
```
###
#### This will print the following:
```
Naruto
Boruto: Naruto Next Generations
Naruto - Full Color
Naruto Gaiden: The Seventh Hokage
Naruto: Chibi Sasuke's Sharingan Legend
```
### 3. Manga Details
```manga_details = get_manga_details(mangaid="Naruto")```
###
#### Manga Details Result
```
{'alternative': 'ナルト (Japanese) ; 火影忍者 (Chinese-Simplified) ; 狐忍 '
                '(Chinese-Traditional) ; ناروتو (Arabic / Persian) ; '
                'นินจาคาถาโอ้โฮเฮะ (Thai) ; নারুতো (Bengali) ; नारुतो (Hindi) '
                '; 나루토 (Korean)',
 'author': 'Kishimoto Masash',
 'description': "Naruto is a manga series from Japan. It's about the story of "
                'a young ninja who wants to become the strongest leader in his '
                'village. The series were produced by Masashi Kishimoto and in '
                '1997 were published. Later this manga was adapted into a TV '
                'anime. This studio also has developed 10 movies as well as a '
                'number of video animations. You can read Naruto manga online, '
                'which until today has sold over 220 copies around the world '
                '(except from Japan in 35 more countries), making it the 3rd '
                'best selling series of manga in history.\xa0When he was a '
                'child, Naruto was isolated from its community. The people in '
                "the village treated him as he was Nine-Tails itself and don't "
                'want him. None in the village had the right to mention the '
                'Nine-Tails, in order to prevent Naruto from finding the '
                'truth. But 12 years later, he finds out the truth from ninja '
                'Mizuki, who told him. Some time later, Naruto becomes a ninja '
                'and usually competes against other teams, and they form a '
                'three-person team by the name Team 7. Like all the other '
                'similar teams in every village, the Team 7 has to complete '
                'missions that are requested by the villagers, ranging from '
                'being bodyguards or doing chores. After participating in a '
                'number of missions, the Team 7 is allowed to take place in an '
                'exam, in order to move up in hierarchy and be able to be '
                'involved in more difficult missions. After 2,5 years, Naruto '
                'returns from training and he continued with his team to fight '
                'the Akatsuki members.When Kishimoto first made the plot of '
                'the story, thought that it was a mess. For example, he '
                'thought that the chakras, along with other hand signs made '
                'Naruto look like a lot of Japanese them, but he believed that '
                'it could be enjoyable for reading. In these particular '
                'series, he actually tried to make his characters to look like '
                'unique ones. Above all he based his main theme on the '
                'Japanese culture and he separated the characters in the '
                'series into different teams, in order to give to each team a '
                'special flavor. He wanted to make each member to look like an '
                "'extreme' character and when he was creating them, Kishimoto "
                'followed the 5 steps, like drafting, sketching, colouring, '
                'inking and shading. Moreover, when he started creating the '
                'series, Kishimoto paid attention to the designs of the '
                'village and the settings. For instance, the village was '
                'created spontaneously, but he took the idea for the scenery '
                'from his home in Okayama, in Japan.The Naruto Anime made its '
                'debut in Japan TV Tokyo in October 2002 and was concluded in '
                '2007 after 220 episodes. In addition, these series led also '
                'led to the production of 10 films. The first one under the '
                "title 'Ninja clash in the land of Snow' was first released in "
                'August 2004 in Japan and told the story fo how Team 7 was '
                'sent to the Land of Snow, in order to protect the actors from '
                "shootings of he new Princess Fun movie.The soundtracks of '' "
                "were composed by T. Masuda. The first under the title 'Naruto "
                "Manga Original Soundtrack' was released in April 2003 and had "
                '22 tracks. In addition, the video games of Naruto, which are '
                'mostly fighting games, were seen in various consoles from '
                'Sony, Microsoft and NintendoOther attractive Manga :',
 'genre': 'Action , Adult , Adventure , Comedy , Doujinshi , Drama , Fantasy , '
          'Martial arts , Shounen',
 'image': 'https://manganelo.tv/mangaimage/manga-ng952689.jpg',
 'status': '                                          Completed',
 'title': 'Naruto Manga',
 'view': '39105035 views'}
```
###
#### Specific Result of Manga Detail
```
View = manga_details.get('view')
print(View)
```

### 4. Manga Episode
```manga_episode = get_manga_episode(mangaid="naruto")```
###
#### Manga Episode Result
```
{'title': 'Naruto', 'totalchapter': '748'}
```
###
#### Total Chapter Result of Manga Detail
```
TotalChapter = manga_details.get('totalchapter')
print(TotalChapter)
```

### 4. Manga Chapter 
```manga_chapter = get_manga_chapter(mangaid="Naruto", chapNumber=2)```
###
#### Manga Episode Result
```
{'totalPages': "['https://cm.blazefast.co/2e/ea/2eeab195b6a26f8bfae825259e998138.jpg', 
'https://cm.blazefast.co/31/1d/311dc632f26386a2c52f7e29dc6e946a.jpg', 
'https://cm.blazefast.co/12/da/12da24bcc395fa5ce279bb170be4d44b.jpg', 
'https://cm.blazefast.co/bc/2f/bc2ffcf64e7c2aaf2f9d6d5d4517fc1c.jpg',
'https://cm.blazefast.co/54/05/540581ecc794f3f826ac9028dcf92837.jpg',
'https://cm.blazefast.co/ee/e1/eee1c6836911aadb929f998647571cc6.jpg',
'https://cm.blazefast.co/46/03/460381c860157df7d7bb5ab89e639123.jpg', 
'https://cm.blazefast.co/19/50/1950e9174dac67c7e2e21d0f7c12cf27.jpg', 
'https://cm.blazefast.co/da/32/da32bdf373ad594bd83b90d7042996e2.jpg', 
'https://cm.blazefast.co/ea/e8/eae8b26f9667391898f55047807f9081.jpg', 
'https://cm.blazefast.co/0b/61/0b6160a66275324f3f61c444f679b53c.jpg', 
'https://cm.blazefast.co/21/5f/215fc812ddbc0e576660bb39a429d461.jpg', 
'https://cm.blazefast.co/27/ed/27ed2b0575db916ed8bf02711d891865.jpg', 
'https://cm.blazefast.co/f7/7a/f77a4d08065225afdb25efa20fab805c.jpg', 
'https://cm.blazefast.co/f7/e8/f7e89774749b4e254f94b20a3a233bc1.jpg', 
'https://cm.blazefast.co/0e/b5/0eb5e5fcab126ac1dea85a9129a4cdfe.jpg', 
'https://cm.blazefast.co/89/ea/89ea59cc75c3e71a29a4708aec881c7f.jpg', 
'https://cm.blazefast.co/07/a7/07a7238c315e1de053736e59a480c205.jpg', 
'https://cm.blazefast.co/bf/3f/bf3fbdb61829e965ceb6be425cb833ea.jpg', 
'https://cm.blazefast.co/4f/24/4f2484a29125a35e83f3dab92834d2e4.jpg', 
'https://cm.blazefast.co/91/54/91541dc4764641740502df1f1386d958.jpg', 
'https://cm.blazefast.co/07/d2/07d2068cf17b9a4fb2f6a5eb4e4c525a.jpg', 
'https://cm.blazefast.co/06/b0/06b0172d20e2e0bb58060da36c9e5568.jpg']"}
```
###
