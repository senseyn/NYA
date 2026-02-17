```
███╗   ██╗██╗   ██╗ █████╗     ██╗    ██╗███████╗██████╗      █████╗ ██████╗ ██████╗ 
████╗  ██║╚██╗ ██╔╝██╔══██╗    ██║    ██║██╔════╝██╔══██╗    ██╔══██╗██╔══██╗██╔══██╗
██╔██╗ ██║ ╚████╔╝ ███████║    ██║ █╗ ██║█████╗  ██████╔╝    ███████║██████╔╝██████╔╝
██║╚██╗██║  ╚██╔╝  ██╔══██║    ██║███╗██║██╔══╝  ██╔══██╗    ██╔══██║██╔═══╝ ██╔═══╝ 
██║ ╚████║   ██║   ██║  ██║    ╚███╔███╔╝███████╗██████╔╝    ██║  ██║██║     ██║     
╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝     ╚══╝╚══╝ ╚══════╝╚═════╝     ╚═╝  ╚═╝╚═╝     ╚═╝  
```

<a id="top"></a>

**Nya** - это удобная картотека фильмов и сериалов, созданная для настоящих киноманов. Забудьте о бесконечном скроллинге и сомнениях в выборе. Наше приложение помогает систематизировать огромный мир контента, предоставляя быстрый доступ к информации о любом фильме или сериале: от актерского состава и рейтингов до трейлеров и похожих картин.

**Nya** - это только начало. Мы видим это приложение не просто как каталог, а как фундамент для будущей экосистемы. В наших планах - превратить Nya в полноценный онлайн-кинотеатр. Мы стремимся к тому, чтобы от выбора фильма до его просмотра вас отделял всего один клик. Следите за обновлениями, чтобы первыми узнать, когда Nya станет вашим главным окном в мир кино!

[![Stars](https://starchart.cc/senseyn/NYA.svg?variant=adaptive)](https://starchart.cc/senseyn/NYA) 

[![Top contributors](https://contrib.rocks/image?repo=senseyn/NYA)](https://github.com/senseyn/NYA.git)


--------
- uses: Platane/snk@v3
  with:
    # github user name to read the contribution graph from (**required**)
    # using action context var `github.repository_owner` or specified user
    github_user_name: ${{ github.repository_owner }}

    # list of files to generate.
    # one file per line. Each output can be customized with options as query string.
    #
    #  supported options:
    #  - palette:           A preset of color, one of [github, github-dark, github-light]
    #  - color_snake:       Color of the snake
    #  - color_dots:        Coma separated list of dots color.
    #                       The first one is 0 contribution, then it goes from the low contribution to the highest.
    #                       Exactly 5 colors are expected.
    #  - color_background:  Color of the background (for gif only)
    outputs: |
      dist/github-snake.svg
      dist/github-snake-dark.svg?palette=github-dark
      dist/ocean.gif?color_snake=orange&color_dots=#bfd6f6,#8dbdff,#64a1f4,#4b91f1,#3c7dd9&color_background=#aaaaaa

<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/senseyn/senseyn/output/github-contribution-grid-snake-dark.svg" />
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/senseyn/senseyn/output/github-contribution-grid-snake.svg" />
    <img alt="github-snake" src="https://raw.githubusercontent.com/senseyn/senseyn/output/github-contribution-grid-snake.svg" />
  </picture>
</div>
-----------
<h1 align="center">
  <a href="#top">| 💔 |</a>
</h1>

