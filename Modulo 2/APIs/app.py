import streamlit as st

musicas = {
        "Justin Bieber": {
        "2 Much": "https://www.youtube.com/watch?v=xFJjczkU4So",
        "Flatline": "https://www.youtube.com/watch?v=YEVcnTIq1us",
    },
    "BTS": {
        "2.0": "https://www.youtube.com/watch?v=_gyultVTesk",
        "On": "https://www.youtube.com/watch?v=gwMa6gpoE9I",
        "Dope":"https://www.youtube.com/watch?v=H8lYMWZD5P8",
    },
    "Michael Jackson": {
        "Billie jean": "https://www.youtube.com/watch?v=Zi_XLOBDo_Y",
        "Heaven can wait": "https://www.youtube.com/watch?v=TDVlDUAIz5k"
    },
     "Ariana Grande": {
        "God is Woman": "https://www.youtube.com/watch?v=kHLHSlExFis",
        "Dangerous Woman": "https://www.youtube.com/watch?v=9WbCfHutDSE",
        "7 Rings":"https://www.youtube.com/watch?v=QYh6mYIJG2Y"
    },
    "The Weeknd": {
        "Coming Down": "https://www.youtube.com/watch?v=WVg1mbxTkFo",
        "Call out my name": "https://www.youtube.com/watch?v=M4ZoCHID9GI",
    },
        "Olivia rodrigo": {
        "Lacy": "https://www.youtube.com/watch?v=VEV21XoU14w",
        "All is Want": "https://www.youtube.com/watch?v=OOgvDiXl6hA",
        "Jealousy,Jealousy":"https://www.youtube.com/watch?v=OOgvDiXl6hA",
        
        },
        "Chase atlantic": {
        "Slow down":"https://www.youtube.com/watch?v=4kbSC3HXfJw",
        "FRIENDS":"https://www.youtube.com/watch?v=nT8O_mP2x6Y",
        "SWIM": "https://www.youtube.com/watch?v=mC9v5FaLt84",
        },

}
st.sidebar.image("logo.png")
artista = st.sidebar.selectbox("Selecione o artista",musicas.keys())
musicas_artista = musicas[artista]

st.title(artista)

video,sobre = st.tabs(['video','sobre'])

with video: 
   for musica in musicas_artista.items():
    titulo, link = musica
    st.subheader(titulo)
    st.video(link)

with sobre:
    if artista == "Justin Bieber":
        st.markdown("nascido em 1994 no Canadá, é um dos maiores ícones pop globais do mundo. Descoberto no YouTube aos 13 anos, ele construiu uma trajetória meteórica marcada pelo sucesso estrondoso de hits mundiais como Baby e Sorry Letras.mus.br, além de uma longa jornada de amadurecimento e desafios pessoais Revista Quem Globo.")
    elif artista == "BTS":
        st.markdown("O BTS é um fenômeno global de K-pop formado em 2013 na Coreia do Sul pela Big Hit Entertainment. O grupo é composto por sete integrantes: RM, Jin, SUGA, j-hope, Jimin, V e Jung Kook. Eles quebram barreiras linguísticas, lideram paradas musicais internacionais e possuem uma base de fãs extremamente dedicada, o ARMY.")
    elif artista == "Michael jackson":
       st.markdown("Michael Jackson (1958–2009) foi um cantor, compositor e dançarino norte-americano, aclamado mundialmente como o Rei do Pop. Ele revolucionou a indústria musical, a dança e os videoclipes, tornando-se uma das figuras culturais mais importantes do século XX com sucessos globais como Thriller — o álbum mais vendido de todos os tempos.")
    elif artista == "Ariana Grande":
       st.markdown("Ariana Grande é uma das maiores cantoras, compositoras e atrizes norte-americanas da atualidade. Nascida em 1993, na Flórida, ela iniciou sua carreira no teatro musical antes de alcançar fama mundial estrelando séries de sucesso na Nickelodeon. Hoje, é conhecida pelo seu impressionante alcance vocal de quatro oitavas e por recordes históricos na indústria da música.")
    elif artista == "The Weeknd":
       st.markdown("The Weeknd é o nome artístico do cantor, compositor e produtor canadense Abel Makkonen Tesfaye. Nascido em Toronto em 1990 e filho de imigrantes etíopes, ele é hoje um dos maiores e mais ouvidos artistas do mundo, conhecido mundialmente por misturar R&B, pop e música eletrônica.")
    elif artista == "Olivia rodrigo":
       st.markdown("Olivia Rodrigo é uma cantora, compositora e atriz norte-americana que se tornou um dos maiores fenômenos da música pop global. Reconhecida por suas letras confessionais e fortes, ela ganhou o público inicialmente como estrela infantil da Disney Channel.")
    elif artista == "Chase atlantic":
       st.markdown("Chase Atlantic é uma banda australiana formada em Cairns, Queensland, e atualmente baseada em Los Angeles. Composta pelos irmãos Mitchel e Clinton Cave, junto com Christian Anthony, o grupo é amplamente conhecido por sua mistura única e envolvente de R&B alternativo, pop, rock e trap.")