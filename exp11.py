import wolframalpha
question=input('question:')
app_id='your app_id'
client=wolframalpha.Client(app_id)
res=Client.query(question)
ans=next(res.result).txt
print(ans)
