import random
import time 
## Introducing the player to the game with some of the info they'll need to get started.
print("Welcome to The Journey.")
print("\n")
name = input("Enter your Name: ")
print("\n")
print("You will start your journey in your senior season of high school cross country. You are a top recruit in the nation looking to commit to an elite program.")
high_school = input("Enter the name of your high school: ")
print("\n")
print("Going into your season you already have three schools you're very interested in. Go ahead and list those schools below.")
print("\n")
school_one = input("School one: ")
school_two = input("School two: ")
school_three = input("School three: ")
print("\n")
print("These schools are interested in you but you must earn a scholarship in order to be on the team. Make the correct decisions and you may even be able to go pro after a collegiate career.")
print("\n")
input("Press enter")
print("\n")
print("Make sure to not only focus on making the correct decisions for running but to stay happy throughout the season so you can continue to run well.")
print("\n")
print("TIP: While answering the questions to choose your path make sure nothing is capitalized and spelling is correct for best results.")
print("\n")
input("Press enter to begin game")
print("\n")
print("First day of practice.")
print("\n")
Q1 = input("Your coach offers you the captain position on your team. Do you accept this responsibility? (yes/no):  ")
print("\n")
## if user answers yes they will go down path number one where all of the questions "Q#" will be odd numbers
if Q1 == "yes":
  Q3 = input("Congratulations on accepting this honor! Your first job as a captain will be to organize a team building activity. What would you rather do (ultimate frisbee/pasta party):  ")
  ## there is a 10% chance on this path that the game could end due to an injury to the main player 
  num = random.randint(1,10)
  if Q3 == "ultimate frisbee":
    if num == 1:
      print("\n")
      print("You stepped in a hole and broke your ankle while playing. Your season and career is over.")
      print("\n")
      print("GAME OVER")
    else:
      print("\n")
      print("Everyone enjoyed the game and you Proved yourself a true leader for the season to come.")
      print("\n")
      print("First meet of the year")
      print("\n")
      Q9 = input("You prepare to run your first meet of your senior season. Do you take it out aggressive or conservative? (aggressive/conservative): ")
      if Q9 == "aggressive":
        print("\n")
        Q19 = input("You take this first race out aggressive. You are in 15th place with a mile left. Do you start pasing other runners or draft to save energy for the last 800M?. (pass/draft): ")
        if Q19 == "pass":
          print("\n")
          print("You've decided to start passing the competition. Everything goes well until you run out of energy in the end. You finsih in 12th place")
          print("\n")
          Q41 = input("While preparing for your next race you're faced with a decision of having to miss practice for a college visit to " + school_three + " or going to practice. What do you do? (visit/practice): ")
          if Q41 == "visit":
            print("\n")
            print("You've decided to go on a visit to " + school_three + ". You skip practice and the visit goes well.")
            print("\n")
            print("Second meet")
            print("\n")
            Q45 = input("You're midway through your race and your legs are feeling extremly tired and tight. You continue to fall back in places. Do you cut your losses and drop out of the race or tough it out? (drop/continue): ")
            if Q45 == "drop":
              print("\n")
              print("You decided to drop. Your coach and teammates are not very happy with you but you did what you thought was right.")
            else:
              print("\n")
              print("You continue on and after the race your right leg is feeling very loose and weird.")
              print("\n")
              print("After a couple days you get your leg ")
          else:
            print("\n")
        else:
          print("\n")
          print("You decide to draft for a while. You actually pass other runners whie drafting and make a strong move in the end. You finish in 6th place.")
          print("\n")
          print("Second meet")
          print("\n")
          Q43 = input("You face a decison on whether or not to take this race out aggressive again or not. You are feeling more hesitant this time around as the number of racers is much higher. Do you go out hard again or hold back? (hard/hold back): ")
          if Q43 == "hard":
            print("\n")
          else:
            print("\n")
      else:
        print("\n")
        Q21 = input("You decide to take this first race out at a safe pace to save more energy for the end. You end up getting boxed in a large group of runners. The only way out is to cut off one of your teammates. Do you stay boxed in or cut off your teammate to break out? (boxed in/cut off): ")
        if Q21 == "boxed in":
          print("\n")
          print("You ended up making your way out of the pack and moved up. It was too little too late though and you only finished in 21st place among the field. On to the next race.")
          print("\n")
          Q25 = input("You are frustrated with how the last race went. Do you have a team meeting to tell your teammates to run better as a team or bite your tongue? (team meeting/bite tongue): ")
          if Q25 == "team meeting":
            print("\n")
            print("You call your team together to tell them to help eachother run better in races. they all understand and respect what you told them.")
            print("\n")
            print("Second race")
            print("\n")
            Q27 = input("You are looking to have a better showing this race. Do you go out aggressive this time or trust your teammates and run as a pack? (aggressive/pack run")
            if Q27 == "aggressive":
              print("\n")
              Q31 = input("You take this race out very aggressive and it is working out for you. You have 800M left. Do you stay aggresive or just hold on to your current postion? (make a move/hold on): ")
              if Q31 == "make a move":
                print("\n")
                print("You make a move and it worked great until the final 50M where you hit a wall. still a great race having you finish 9th.")
                print("\n")
                print("You have one final chance to impress college coaches.")
                print("\n")
                print("STATE MEET")
                print("\n")
                Q39 = input("You're hoping to be able to make a little bit of magic happen and earn all-state honors. Do you race aggressive to do this or hold back and be strategic? (aggressive/strategic): ")
                if Q39 == "aggressive":
                  print("\n")
                  print("You decided ")
                else:
                  print("\n")
              else:
                print("\n")
                print("You decided to try and hold on to your current postion. Lucky for you the rest of the field seemed to hit a wall and you move up. You finish in 4th place.")
                print("\n")
                print("You're feeling good with your improvement from the last race. You're looking to make a statement this week in your final meet of the year.")
                print("\n")
                print("STATE MEET")
                print("\n")
                print("Your final meet of your highschool career. you're hoping to finish your highschool career with all state honors...")
                print("\n")
                Q33 = input("This is the largest field you have run against. Do you make an effort to make sure to get out in front of everyone so you don't get boxed in or run your race? (get out/run your race): ")
                if Q33 == "get out":
                  print("\n")
                  Q35 = input("You get out quick to lead the field. Your chest is starting to tighten up. Do you conceed the lead to save your lungs or hold on and hope for the best? (slow up/hope for the best): ")
                else:
                  print("\n")
                  Q37 = input("You decided to run your own race from the jump. You have 400M to go and you're 25th, the last all state honor spot. your legs are tired from having to weave through everyone in the race. Do you push yourself or be conservative? (push it/hold back): ")
                  if Q37 == "push it":
                    print("\n")
                    print("you gave everything you had in the last 400M and it payed off. You defended your postion and finished 25th.")
                    print("\n")
                    print("ALL STATE HONORS")
                    print("...")
                    print("23. Mark Andrews")
                    print("24. Jeremy Green")
                    print("25. " + name)
                    print("\n")
                    print("After finishing all state you have recieved offers from " + school_two + " and " + school_three +".")
                    print("\n")
                    print("to be continued...")
                  else:
                    print("\n")
                    print("You held back and just missed your goal of being all state finishing 26th...")
                    print("\n")
                    print("Your season is now over. After finishing just out of your goal you lost your love for running and decided to no longer pursue a college career.")
                    print("\n")
                    print("GAME OVER")
            else:
              print("\n")
          else:
            print("\n")
            print("You decide to bite your tongue and feel it's better you don't lecture your team on teamwork.")
            print("\n")
            print("Second race")
            print("\n")
            Q29 = input("This second race you are looking to ")
        else:
          print("\n")
          print("You try to breakout out of the group by cutting off one of your teammates. You end up getting tangled up with your teammate and you both fall. You do not finish the race.")
          print("\n")
          print("You tore a calf muscle during your last race and will miss your next race. You now only have one race remaining to impress a coach.")
          print("\n")
          print("Final meet")
          print("\n")
          Q23 = input("This is your last chance to impress a coach. Your calf is still feeling a little sore. Do you take this next race more aggressive or hold back to keep your calf healthy? (aggressive/play it safe): ")
          if Q23 == "aggressive":
            print("\n")
            print("")
          else:
            print("\n")
            print("")
  else:
    print("\n")
    Q7 = input("You invited your whole team over to your house for a pasta party and everyone is having fun. They want you to go with them to TP a rivals school runners house. Do you go with them? (go/dont): ")
    if Q7 == "go":
      print("\n")
      Q11 = input("You go with your team and TP the runners house. Their parents came out and you all start to run away! Do you run to your car or hide in a nearby bush? (car/bush): ")
    else:
      print("\n")
      print("You decided not to go and stay at home instead.")
      print("\n")
      print("First meet of the year")
      print("\n")
      Q13 = input("You just finished an easy run before your first meet. Do you ice bath before the meet or just go home to rest tonight? (ice bath/rest):  ")
      if Q13 == "ice bath":
        print("\n")
        Q15 = input("")
      else:
        print("\n")
        Q17 = input("")
        ## This is the start of the second option where all of the questions "Q#" will be even numbers
else:
  print("\n")
  Q2 = input("You decide not to accept the position and focus on yourself for the season. Practice is starting up and you are deciding between running with the other varsity runners or doing your own thing and running ahead of them to train harder. What will you do? (run with group/do my own thing):  ")
  if Q2 == "run with group":
    print("\n")
    print("You decide to run with your other varsity runners. You all continue to push each other to get better.")
    print("\n")
    print("First meet of the year")
    print("\n")
    Q4 = input("You just finished an easy run before your first meet. Do you ice bath before the meet or just go home to rest tonight? (ice bath/rest): ")
    if Q4 == "ice bath":
      print("\n")
      Q8 = input("You decided to take the ice bath and suffer through the cold. When you get home you remember you have a paper you haven't done yet at 11:59. Do you go to bed to be well rested for the meet or work on your paper to turn it in? (sleep/write paper): ")
      if Q8 == "sleep":
        print("\n")
        print("You choose to get some sleep and be well rested.")
        print("\n")
        print("meet day")
        print("\n")
        Q10 = input("")
      else:
        print("\n")
        input("You decided to stay up and write the paper and turned it in just in time! You still have to get your running gear around so it'll be a late night.")
        print("\n")
    else:
      print("\n")
      input("You decided to go home to rest.")
      print("\n")
  else:
    print("\n")
    print("You decided to do your own thing and run ahead of the group to push yourself.")
    print("\n")
    print("First meet of the year")
    print("\n")
    Q6 = input("You just finished an easy run before your first meet. Do you ice bath before the meet or just go home to rest tonight? (ice bath/rest): ")
    if Q6 == "ice bath":
      print("\n")
      print("You choose to take an ice bath")
      print("\n")
      print("First meet of the year")
      print("\n")
      Q12 = input("You'll need to set the tone for the rest of the season. Do you go out hard and push for the front or stay conservative and stay consistent throughout the race? (aggressive/ conservative)")
      if Q12 == "aggressive":
        print("\n")
        Q14 = input("You are running great and are 5th with half a mile left. do you push for the lead now or wait till the last 100M? (now/wait)")
        if Q14 == "now":
          print("\n")
          print("You go with half a mile to go and have an amazing finish to win the race!!")
          Q22 = input("Do you go out and celebrate your victory at a party or move on to the next race? (party/move on)")
          if Q22 == "party":
            print("\n")
            print("You decide to go out and party. The party gets busted but you run and make it home safe.")
            print("\n")
            print("Second Meet of the year")
            print("\n")
            Q26 = input("Your leg is feeling a little sore from when you ran from the cops. Do you take this race out a little slower to feel out your leg or keep with your aggressive start? (go easy/aggressive): ")
        else:
          print("\n")
          print("You wait till the last 100M and make a move that bumps you up. You finish 3rd with a great PR.")
          Q24 = input("After your 3rd place finish are you satisfied and take the rest of the day off and take it easy or are you unsatisfied and go for another training run to try and get closer to winning races? (rest/run)")
          if Q24 == "rest":
            print("\n")
            print("You take the rest of the day off.")
            print("\n")
            print("Second meet of the year")
            print("\n")
            print("You're looking to make")
          else:
            print("\n")
            print("You are unsatisfied with the results and decide to run again. You end up overworking your body and get a stress fracture ending your season")
            print("\n")
            print("GAME OVER")  
      else:
        print("\n")
        Q16 = input("You wait back and get caught in a large group with 1 mile left. Do you break out and let loose or stay conservative? (let loose/conservative)")
        if Q16 == "let loose":
          print("\n")
          print("you decide to let loose and you make up a lot of ground but you waited too long. You finish 27th place, 2 away from medaling.")
          Q18 = input("After your rough race one of the coaches recruiting you calls you. Do you answer the phone or ignore the call? (answer/ignore)")
        else:
          print("\n")
          print:("You decided to stay conservative. You finish in the middle of the pack and your college hopes aren't looking great.")
          Q20 = input("You need to do something to move up in the pack quick. Do you talk to your coach about adding more mileage in training or about changing race strategy? (mileage/strategy)")
          if Q20 == "mileage":
            print("\n")
            print("You talk to your coach about adding mileage to your training. You over work your body and are unable to perform the rest of the season")
            print("\n")
            print("GAME OVER")
          else:
            print("\n")
            Q26 = input("You talk to your coach about changing your strategy where he recommends going out harder. Do you take his advice or keep your old strategy? (take advice/ignore)")
            if Q26 == "take advice":
              print("\n")
              print("Second meet of the year")
              print("\n")
              Q28 = input("It's time to take the advice of your coach and go out harder. Do you follow through with your new strategy? (yes/no)")
              if Q28 == "yes":
                print("\n")
                Q34 = input("Your new strategy sets you up much better for the last 400M. Your are in 12th place with time to make one final move. Do you start your kick now or wait until 200M left? (now/wait)")
                if Q34 == "now":
                  print("\n")
                  print("You go now which is a tad too early. You die off in the end but still gain one position to finish 11th.")
                  print("\n")
                  print("You are now moving onto your final race of the season. The state meet. This is the best time to impress your colleges.")
                  print("\n")
                  print("STATE MEET")
                  print("\n")
                  Q36 = input("")
              else:
                print("\n")
                Q32 = input("You once again start the race conservative and are stuck in the middle of the pack. You become frustrated, do you drop out of the race or continue? (drop/continue)")
            else:
              print("\n")
              print("Second meet of the year")
              print("\n")
              Q30 = input("You once again start the race conservative and are stuck in the middle of the pack yet again. You become frustrated, do you drop out of the race or continue? (drop/continue)")
              if Q30 == "drop":
                print("\n")
                print("You decided to drop out of the race. You only have one more opportunity to impress your college coaches.")
                print("\n")
                print("Final meet of the year")
                print("\n")
                Q38 = input("This is your last chance of the year to make something happen. Do you decide to go aggressive or stay to your normal strategy? (aggressive/normal): ")
                if Q38 == "normal":
                  print("\n")
                  print("You did not make any adjustments to your race strategy and you had the same outcome as the other races.")
                  print("\n")
                  print("The definition of insanity is doing the same thing over and over again, but expecting different results.")
                  print("\n")
                  print("GAME OVER")
                else:
                  print("\n")
                  print("You finally decided to be aggressive but it was too little too late. Your college offers have already been pulled.")
                  print("\n")
                  print("GAME OVER")
              else:
                print("\n")
                print("you decide to continue running the race and finish 32nd overall. You have one last opportunity to impress college coaches.")
                print("\n")
                print("Final meet of the year")
                print("\n")
                Q40 = input("This is your last opportunity to make a college coach impressed. Do you switch your race strategy to a more aggressive approach or stick with a steady race? (aggressive/steady): ")
                if Q40 == "aggressive":
                  print("\n")
                  Q42 = input("Your race goes much better and you are in the top 10 halfway through the race. Do you stay aggressive and keep moving up or do you become conservative to try and hold onto this position? (aggressive/conservative): ")
                  if Q42 == "aggressive":
                    print("\n")
                    print("You moved all the way up to 3rd place before having to pull of the course and puke. You continued running but ended all the way back in 40th place.")
                    print("\n")
                    print("You had a good season.")
                    print("\n")
                    print("Just not good enough...")
                    print("\n")
                    print("GAME OVER")
                  else:
                    print("\n")
                    print("You played it safe and it worker out. You finish in 8th place.")
                    print("\n")
                    print("Your season is now over. Time to see if any coaches offered you...")
                    print("\n")
                    print("You received an offer of a partial scholarship from " + school_three + "! Congratulations! You're ready for the next step in your running career.")
                    print("\n")
                    print("To be continued...")
                else:
                  print("\n")
                  print("You stay conservative and get the same results as every other meet. You get no college offers.")
                  print("\n")
                  print("The definition of insanity is doing the same thing over and over, but expecting different results.")
                  print("\n")
                  print("GAME OVER")