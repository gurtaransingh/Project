{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Youtube Video Info and Download",
      "provenance": [],
      "mount_file_id": "1zWtXJBavei8VDhMOrSH2KQ926Yp5rTvq",
      "authorship_tag": "ABX9TyMOZdN/4B6iZRx6u2h5/OCs",
      "include_colab_link": true
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
        "<a href=\"https://colab.research.google.com/github/gurtaransingh01/Project/blob/main/YT_Video_Info_and_Download.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 14,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "1jcYb82Rcton",
        "outputId": "23cbbc34-d426-45fc-c31b-9b6bb595e401"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "2022-06-20 09:58:06.544 INFO    numexpr.utils: NumExpr defaulting to 2 threads.\n",
            "2022-06-20 09:58:08.482 \n",
            "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
            "  command:\n",
            "\n",
            "    streamlit run /usr/local/lib/python3.7/dist-packages/ipykernel_launcher.py [ARGUMENTS]\n"
          ]
        }
      ],
      "source": [
        "from multiprocessing.sharedctypes import Value\n",
        "import streamlit as st\n",
        "import time\n",
        "from time import *\n",
        "\n",
        "st.title(\"Title\")\n",
        "\n",
        "st.header(\"hello\")\n",
        "\n",
        "st.subheader(\"sub header\")\n",
        "\n",
        "st.text(\"hemlo and welcome to streamil\")\n",
        "\n",
        "# st.latex('''x^2''')\n",
        "\n",
        "if st.button(\"RUN\"):\n",
        "    st.write(\"GGs\")\n",
        "\n",
        "name = st.text_input(\"Name\")\n",
        "\n",
        "dob = st.date_input(\"DOB\")\n",
        "\n",
        "time = st.time_input(\"TOB\")\n",
        "\n",
        "add = st.text_area(\"POB\")\n",
        "\n",
        "st.checkbox(\"Agree to terms and conditions:\", value=False)\n",
        "\n",
        "rd = st.radio(\"color\",[\"R\",\"B\",\"G\"],index=0)\n",
        "st.write(rd)\n",
        "\n",
        "st.selectbox(\"color\",[\"Select color\",\"R\",\"B\",\"G\"],index=0)\n",
        "\n",
        "st.multiselect(\"color\",[\"R\",\"B\",\"G\"])\n",
        "\n",
        "st.slider(\"Age\",min_value=10,max_value=20,value=15,step=2)\n",
        "\n",
        "st.number_input(\"Age\",min_value=10,max_value=20,value=15,step=1)\n",
        "\n",
        "kek = st.file_uploader(\"Drop your file here\")\n",
        "\n",
        "# st.write(kek)\n",
        "\n",
        "st.sidebar.selectbox(\"Select a number\",[1,2,3,4,5,6,7,8,9,0])\n",
        "\n",
        "ram = st.sidebar.radio(\"okbai\",[1,2])\n",
        "\n",
        "if ram ==2:\n",
        "\n",
        "    progress = st.progress(0)\n",
        "    for i in range(0,100):\n",
        "        time.sleep(0.1)\n",
        "        progress.progress(i+1)\n",
        "\n",
        "\n",
        "    st.error(\"Error\")\n",
        "    st.success(\"Show sucess\")\n",
        "    st.info(\"Info\")\n",
        "    st.exception(RuntimeError(\"Runtime Error\"))\n",
        "    st.warning(\"This is a warning\")\n",
        "\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "pip install pytube\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "xr1mln_tgdMW",
        "outputId": "f5412ae3-236a-4153-b0c4-645de44c91c7"
      },
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/\n",
            "Requirement already satisfied: pytube in /usr/local/lib/python3.7/dist-packages (12.1.0)\n"
          ]
        }
      ]
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
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "vZbftNATeZCs",
        "outputId": "2bf99400-e2b8-42c0-b352-8a4e5aca0d9c"
      },
      "execution_count": 10,
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Enter Link of Youtube Video: https://youtu.be/9V3Qdow1Eh4\n"
          ]
        }
      ]
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
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "mZB_slnCebPC",
        "outputId": "01e39af2-60ca-4e76-cbe0-59834e66b119"
      },
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Title : IoT sensor Modules 1\n",
            "Views : 1238\n",
            "Duration : 2721\n",
            "Description : Sensor modules for IoT applications\n",
            "Ratings : None\n"
          ]
        }
      ]
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
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "KmTTKFauoJ-8",
        "outputId": "d28a4c18-e68c-487e-ac10-f044a59e9fd0"
      },
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Download completed!!\n"
          ]
        }
      ]
    }
  ]
}