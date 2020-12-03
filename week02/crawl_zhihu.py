import requests
import json
import os
from pathlib import *
import threading
  
def saveQuestionDB(id, title, url, answer):
    # filePath = Path(os.getcwd()).resolve().parent.joinpath( id + '_question.txt')
    filePath = Path(os.getcwd()).resolve().joinpath( id + '_question.txt')
    
    with open( filePath , 'a', encoding='utf-8') as pipeline_f:
        # 解析方法和scrapy相同，再构造一个json
        response = {
            'id': id,
            'title': title,
            'answer': answer,
            'url': url
        }
        json.dump(response ,pipeline_f, ensure_ascii=False)

 
def saveArticleDB(id, title, vote, cmts, auth, url):
    filePath = Path(os.getcwd()).resolve().joinpath( id + '_article.txt')
    
    with open( filePath , 'a', encoding='utf-8') as pipeline_f:
        # 解析方法和scrapy相同，再构造一个json
        response = {
            'id': id,
            'title': title,
            'vote': vote,
            'cmts': cmts,
            'auth': auth,
            'url': url
        }
        json.dump(response ,pipeline_f, ensure_ascii=False)
 
def fetchResult(url):
    # 发起网络请求，获取数据
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    }
 
    # 发起网络请求
    r = requests.get(url,headers=headers)
    r.encoding = 'Unicode'
    return r.text
 
def parseJson(text):
    json_data = json.loads(text)

    if json_data is None:
        return

    itemList = json_data['data']
    nextUrl = json_data['paging']['next']
    
    if not itemList:
        return
 
    for item in itemList:
        type = item['target']['type']
        
        if type == 'answer':
            # 回答
            question = item['target']['question']
            answer = item['target']['content']
            id = question['id']
            title = question['title']
            url = 'https://www.zhihu.com/question/' + str(id)
            print("问题：",id,title, answer)
            # 保存到数据库
            saveQuestionDB(str (id),title,url, answer)
 
        elif type == 'article':
            #专栏
            zhuanlan = item['target']
            id = zhuanlan['id']
            title = zhuanlan['title']
            url = zhuanlan['url']
            vote = zhuanlan['voteup_count']
            cmts = zhuanlan['comment_count']
            auth = zhuanlan['author']['name']
            print("专栏：",id,title)
            # 保存到数据库
            saveArticleDB( str (id), title, vote, cmts, auth, url)
 
        elif type == 'question':
            # 问题
            question = item['target']
            id = question['id']
            title = question['title']
            url = 'https://www.zhihu.com/question/' + str(id)
            print("问题：",id,title)
            # 保存到数据库
            saveQuestionDB(str (id),title,url)
    return nextUrl
 
def crawl_1(topicID, top=15):
    '''top_activity'''

    url = 'https://www.zhihu.com/api/v4/topics/' + topicID + '/feeds/top_activity?limit=' + top + '&include=data%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Danswer%29%5D.target.content%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%3Bdata%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Danswer%29%5D.target.is_normal%2Ccomment_count%2Cvoteup_count%2Ccontent%2Crelevant_info%2Cexcerpt.author.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Darticle%29%5D.target.content%2Cvoteup_count%2Ccomment_count%2Cvoting%2Cauthor.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Dpeople%29%5D.target.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Danswer%29%5D.target.annotation_detail%2Ccontent%2Chermes_label%2Cis_labeled%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Canswer_type%3Bdata%5B%3F%28target.type%3Danswer%29%5D.target.author.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Danswer%29%5D.target.paid_info%3Bdata%5B%3F%28target.type%3Darticle%29%5D.target.annotation_detail%2Ccontent%2Chermes_label%2Cis_labeled%2Cauthor.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Dquestion%29%5D.target.annotation_detail%2Ccomment_count%3B&limit=10&after_id=0'
    count = 0
    while url and count <= 10 :
        text = fetchResult(url)
        url = parseJson(text)
        count = count + 1
        # print("crawl_1")
 
def crawl_2(topicID, top=15):
    '''essence'''

    url = 'https://www.zhihu.com/api/v4/topics/' + topicID + '/feeds/essence?limit=' + top + '&include=data%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Danswer%29%5D.target.content%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%3Bdata%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Danswer%29%5D.target.is_normal%2Ccomment_count%2Cvoteup_count%2Ccontent%2Crelevant_info%2Cexcerpt.author.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Darticle%29%5D.target.content%2Cvoteup_count%2Ccomment_count%2Cvoting%2Cauthor.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Dpeople%29%5D.target.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Danswer%29%5D.target.annotation_detail%2Ccontent%2Chermes_label%2Cis_labeled%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Canswer_type%3Bdata%5B%3F%28target.type%3Danswer%29%5D.target.author.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Danswer%29%5D.target.paid_info%3Bdata%5B%3F%28target.type%3Darticle%29%5D.target.annotation_detail%2Ccontent%2Chermes_label%2Cis_labeled%2Cauthor.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Dquestion%29%5D.target.annotation_detail%2Ccomment_count%3B&limit=10&offset=0'
    count = 0
    while url and count <= 10 :
        text = fetchResult(url)
        url = parseJson(text)
        count = count + 1
        # print("crawl_2")
 
def crawl_3(topicID, top=15):
    '''top_question'''

    url = 'https://www.zhihu.com/api/v4/topics/' + topicID + '/feeds/top_question?limit=' + top + '&offset=0&include=data%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Danswer%29%5D.target.content%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%3Bdata%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Danswer%29%5D.target.is_normal%2Ccomment_count%2Cvoteup_count%2Ccontent%2Crelevant_info%2Cexcerpt.author.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Darticle%29%5D.target.content%2Cvoteup_count%2Ccomment_count%2Cvoting%2Cauthor.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Dpeople%29%5D.target.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Danswer%29%5D.target.annotation_detail%2Ccontent%2Chermes_label%2Cis_labeled%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Canswer_type%3Bdata%5B%3F%28target.type%3Danswer%29%5D.target.author.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Danswer%29%5D.target.paid_info%3Bdata%5B%3F%28target.type%3Darticle%29%5D.target.annotation_detail%2Ccontent%2Chermes_label%2Cis_labeled%2Cauthor.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Dquestion%29%5D.target.annotation_detail%2Ccomment_count%3B&limit=10&offset=0'
    count = 0
    while url and count <= 10 :
        text = fetchResult(url)
        url = parseJson(text)
        count = count + 1
        # print("crawl_3")
 
if __name__ == '__main__':
    topicID = input('input topic id, e.g. 20192351 - 肖战 >>') 
    try:
        # t1 = threading.Thread(target=crawl_1, args=(topicID, str(15))) #讨论
        t2 = threading.Thread(target=crawl_2, args=(topicID, str(15) )) #精华
        # t3 = threading.Thread(target=crawl_3, args=(topicID, str(15))) #等待回答
        # t1.start()
        t2.start()
        # t3.start()
    except:
       print ("Error: 无法启动线程")