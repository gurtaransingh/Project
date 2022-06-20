{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Youtube Video Info and Download",
      "provenance": [],
      "mount_file_id": "1zWtXJBavei8VDhMOrSH2KQ926Yp5rTvq",
      "authorship_tag": "ABX9TyMmq+prVDEOa2zwIjK+7pAO",
#       "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/gurtaransingh01/Project/blob/main/Youtube_Video_Info_and_Download.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
#       "execution_count": null,
      "metadata": {
        "id": "1jcYb82Rcton"
      },
      "outputs": [],
      "source": [
        "pip install streamlit"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "pip install pytube\n"
      ],
      "metadata": {
        "id": "xr1mln_tgdMW"
      },
#       "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "from pytube import YouTube\n",
        "link = input(\"Enter Link of Youtube Video: \")\n",
        "yt = YouTube(link)\n"
      ],
      "metadata": {
        "id": "vZbftNATeZCs"
      },
#       "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "# To print title\n",
        "print(\"Title :\", yt.title)\n",
        "# To get number of views\n",
        "print(\"Views :\", yt.views)\n",
        "# To get the length of video\n",
        "print(\"Duration :\", yt.length)\n",
        "# To get description\n",
        "print(\"Description :\", yt.description)\n",
        "# To get ratings\n",
        "print(\"Ratings :\", yt.rating)\n"
      ],
      "metadata": {
        "id": "mZB_slnCebPC"
      },
#       "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "stream = yt.streams.get_highest_resolution()\n",
        "stream.download()\n",
        "print(\"Download completed!!\")"
      ],
      "metadata": {
        "id": "KmTTKFauoJ-8"
      },
#       "execution_count": null,
      "outputs": []
    }
  ]
}
