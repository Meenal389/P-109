import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import pandas as pd

df = pd.read_csv('StudentsPerformance.csv')
readingScoreList = df['reading score'].tolist()
mathScoreList = df['math score'].tolist()
writingScoreList = df['writing score'].tolist()

scoreList = []

for i in range(0,len(readingScoreList)-1):
    score = round(statistics.mean([readingScoreList[i],writingScoreList[i],mathScoreList[i]]),2)
    scoreList.append(score)

mean = statistics.mean(scoreList)
median = statistics.median(scoreList)
mode = statistics.mode(scoreList)
stdDev = statistics.stdev(scoreList)

print("Mean: "+str(mean))
print("Median: "+str(median))
print("Mode: "+str(mode))
print("Standard Deviation:  "+str(stdDev))

startStdDev1,endStdDev1 = mean-stdDev,mean+stdDev
startStdDev2,endStdDev2 = mean- 2*stdDev,mean+ 2*stdDev
startStdDev3,endStdDev3 = mean- 3*stdDev,mean+ 3*stdDev
startStdDev4,endStdDev4 = mean- 4*stdDev,mean+ 4*stdDev

fig = ff.create_distplot([scoreList],['Score'],show_hist=False,colors=['#22628e'])


dataInstdDev1 = [result for result in scoreList if startStdDev1<result<endStdDev1]
dataInstdDev2 = [result for result in scoreList if startStdDev2<result<endStdDev2]
dataInstdDev3 = [result for result in scoreList if startStdDev3<result<endStdDev3]
dataInstdDev4 = [result for result in scoreList if startStdDev4<result<endStdDev4]

fig.add_trace(go.Scatter(x = [mean,mean],y = [0,0.03],mode = 'lines',name = 'MEAN',line_color = '#00feff'))

fig.update_layout(title_text = 'Overall Performance of Students')

fig.add_trace(go.Scatter(x = [startStdDev1,startStdDev1],y = [0,0.03],mode = 'lines',name = 'Standard Deviation 1',line_color = '#ae0038'))
fig.add_trace(go.Scatter(x = [endStdDev1,endStdDev1],y = [0,0.03],mode = 'lines',name = 'Standard Deviation 1',line_color = '#ae0038'))
fig.add_trace(go.Scatter(x = [startStdDev2,startStdDev2],y = [0,0.03],mode = 'lines',name = 'Standard Deviation 2',line_color = '#f3001d'))
fig.add_trace(go.Scatter(x = [endStdDev2,endStdDev2],y = [0,0.03],mode = 'lines',name = 'Standard Deviation 2',line_color = '#f3001d'))
fig.add_trace(go.Scatter(x = [startStdDev3,startStdDev3],y = [0,0.03],mode = 'lines',name = 'Standard Deviation 3',line_color = '#ffa200'))
fig.add_trace(go.Scatter(x = [endStdDev3,endStdDev3],y = [0,0.03],mode = 'lines',name = 'Standard Deviation 3',line_color = '#ffa200'))

print("{}% of data lies within Standard Deviation 1".format((len(dataInstdDev1)*100.0/len(scoreList))))
print("{}% of data lies within Standard Deviation 2".format(len(dataInstdDev2)*100.0/len(scoreList)))
print("{}% of data lies within Standard Deviation 3".format(len(dataInstdDev3)*100.0/len(scoreList)))
print("{}% of data lies within Standard Deviation 4".format(len(dataInstdDev4)*100.0/len(scoreList)))

fig.show()