from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import game.models
import json
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView

def showBoard(token):
    board = game.models.showBoard(token)
    return board
def addToBoard(p1,p2,p3,token):
	global board
	if board[p1][p2][p3] == '_':
		board[p1][p2][p3] = str(token)
def index(request):
    return HttpResponse(showBoard(''))
def get(request, token):
    token = str(token)
    board = showBoard(token)
    turn = game.models.checkTurn(token)
    winningPlayer = game.models.checkWinningPlayer()
    if board != False:
        yourTurn = 'not'
        if turn == True:
            yourTurn = ''
        if winningPlayer == False:
            result = 'Welcome player ' + token + '<br> It is '+yourTurn+' your turn<br>'
        else:
            result = 'Player ' + str(winningPlayer) + ' wins<br>'
            result += '<a href="/game/clear/'+str(token)+'">Play again? </a><br>'
        data = json.loads(board)
        itemLevel = 0
        for level in data:
            result += '<table border=1>'
            itemRow = 0
            for row in level:
                result += '<tr>'
                itemCol = 0
                for col in row:
                    if col == '_' and turn == True and winningPlayer == False:
                        result += '<td><a href="/game/put/'+str(itemLevel)+'/'+str(itemRow)+'/'+str(itemCol)+'/'+str(token)+'">_</a></td>'
                    else:
                        result += '<td>'+str(col)+'</td>'
                    itemCol += 1
                itemRow +=1
                result += '</tr>'
            result = result + '</table>'  
            itemLevel += 1
    else:
        result = 'Maximum players reached'
    return HttpResponse(result)

def put(request, level, row, col, token):
    game.models.addToBoard(level,row,col,token)
    return HttpResponseRedirect('/game/get/'+str(token))
def clear(request, token):
    game.models.clearBoard()
    return HttpResponseRedirect('/game/get/'+str(token))