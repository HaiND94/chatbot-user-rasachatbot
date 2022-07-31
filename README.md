# Chatbot_new



## Getting started

To make it easy for you to get started with, here's a list of recommended next steps.

Already a pro? In the first you need to install envirment require follow comment

## Install env

```
pip install -r requirements.txt
pip install https://gitlab.com/trungtv/vi_spacy/-/raw/master/vi_core_news_lg/dist/vi_core_news_lg-0.0.1.tar.gz


```

## To check data vadiate run

```
rasa data validate
```

## To trainning nlu

```
rasa train nlu
```

## To trainning rasa

```
rasa train
```

## To test rasa

```
rasa shell
```

## Enable rasa chatbot server

```
rasa run --cors "*" --enable-api
rasa run actions
```