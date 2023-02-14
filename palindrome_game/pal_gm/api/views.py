import json
from xml.dom import ValidationErr
from django.shortcuts import render
from rest_framework import viewsets
from api.models import User,Game
from api.serializers import UserSerializer,GameSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import JsonResponse
import random
from rest_framework import status
# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class=UserSerializer
# users/{userId}/games
#http://127.0.0.1:8000/api/v1/user/{user_id}/users/
    @action(detail=True,methods=['get'])
    def users(self, request,pk=None):
        print("gate games of user",pk)
        
        user=User.objects.get(pk=pk)
        games=Game.objects.filter(user=user)
        games_serializer=GameSerializer(games,many=True,context={'request':request})
        return Response(games_serializer.data)
    # @api_view(["POST"])
    
    # def login_user(request):

    #     data = {}
    #     reqBody = json.loads(request.body)
    #     phone_no1 = reqBody['hone_no']
    #     print(phone_no1)
    #     password = reqBody['password']
    #     try:

    #         Account = User.objects.get(phone_no=phone_no1)
    #     except BaseException as e:
    #         raise ValidationError({"400": f'{str(e)}'})

    #     token = Tokens.objects.get_or_create(user=Account)[0].key
    #     print(token)
    #     if not check_password(password, Account.password):
    #         raise ValidationError({"message": "Incorrect Login credentials"})

    #     if Account:
    #         if Account.is_active:
    #             print(request.user)
    #             login(request, Account)
    #             data["message"] = "user logged in"
    #             data["email_address"] = Account.email

    #             Res = {"data": data, "token": token}

    #             return Response(Res)

    #         else:
    #             raise ValidationError({"400": f'Account not active'})

    #     else:
    #         raise ValidationErr({"400": f'Account doesnt exist'})
        

class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class=GameSerializer

# game/{game_id}/updateBoard/
    @action(detail=True,methods=['get','post'])
    def updateBoard(self,request,pk=None):
        def isPalindrome(s):
                        return s == s[::-1]
        # board += str(random.randint(0, 9))
        game = Game.objects.get(pk=pk)
        # x=str(random.randint(0, 9))
        # strg=game.game_string
        # game.set_string(x)
        # print(strg,x,"******************")
        data = GameSerializer(instance=game, data=request.data,context={'request': request})
        
        if data.is_valid():
            
            data.save()
            
            game1 = Game.objects.get(pk=pk)
            # s=game.game_string.join(str(random.randint(0, 9)))
            game1.set_string(str(random.randint(0, 9)))
            game1.save()
            # print(game1.game_string)
            game2 = Game.objects.get(pk=pk)
            data1 = GameSerializer(instance=game2, data=request.data,context={'request': request})  
            if data1.is_valid():
            # print(game2.game_string,"$$$$$$$$$$$$")
                if(len(game2.game_string) ==6):
                        
                        s =game2.game_string
                        ans = isPalindrome(s)
                        if ans:
                                return Response("Palindrome")
                        else:
                                return Response("Not Palindrome")
                else:    
                    return Response(data1.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        