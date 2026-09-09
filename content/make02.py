import json
from pathlib import Path
from build_bank import q
sections=[]
def section(title,kind,text,items):
 s={'title':title,'kind':kind,'questions':[q(*x) for x in items]}
 if kind.startswith('listen'):s.update(transcript=text,audio=f'./audio/02-{len(sections)+1}.mp3')
 else:s['text']=text
 sections.append(s)
section('听力 A · 1—4','listenA',"""M: Sophie, have you booked the train tickets for our trip to Greenford?
W: Not yet. The early train is cheaper, but it gets in at eight, and the exhibition doesn't open until ten.
M: We could have breakfast near the station.
W: True, but the cafe we liked has closed. Also, the exhibition is at the university this year, not the town hall. We'd need another bus journey.
M: I hadn't realised that. What about the nine o'clock train?
W: It arrives at ten fifteen. There's a direct bus from the station, so we should reach the university before eleven.
M: That works. I mainly want to hear the photographer's talk at midday.
W: The talk has moved to one because her flight was changed. The ticket still says twelve, but I checked with the organiser this morning.
M: Good thing you did. Shall I book our return journey?
W: Please. Choose a train after five. I'd like enough time to look at the student projects after the talk.
M: All right. I'll send you the booking details tonight.
W: Thanks. I'll bring sandwiches this time. Then we won't spend half our visit searching for somewhere to eat.""",[
(1,'Why does Sophie hesitate to take the early train?',['It arrives much earlier than necessary.','It does not stop at Greenford.','It costs more than the later train.','It requires two changes.'],'A','八点到，十点才开门；主要顾虑是过早到达。'),
(2,'Where will the exhibition take place?',['At the town hall.','At the station.','At the university.','At a photography shop.'],'C','this year at the university；town hall是旧地点。'),
(3,"When will the photographer's talk begin?",['Eleven.','Twelve.','Ten fifteen.','One.'],'D','改到一点，票面十二点是过时信息。'),
(4,'What will the man do?',['Prepare sandwiches.','Book the return tickets.','Contact the photographer.','Arrange a student project.'],'B','女子要求他预订五点以后的回程票。')])
section('听力 A · 5—8','listenA',"""W: Hello, I'm calling about the evening swimming course. I can swim a little, but I get nervous in deep water.
M: Our confidence class would probably suit you. It isn't for complete beginners, but you don't need to be a strong swimmer.
W: Is it the course on Tuesday?
M: Tuesday is for children. The adult class meets on Thursday, from seven to eight. We keep the group small, with no more than eight people.
W: I finish work at six thirty. Would arriving ten minutes late be a problem?
M: The first ten minutes are spent warming up beside the pool. They're important, so we'd rather you attended the whole session. There's also a Saturday morning group.
W: Saturday would be easier. How much does it cost?
M: Forty pounds for four sessions. Equipment is provided, but you'll need your own swimming cap.
W: Can I try one session before paying for the course?
M: Certainly. A trial costs twelve pounds. If you then join, we'll deduct that amount from the course fee.
W: That sounds fair. Could you reserve a trial place for Saturday?
M: Yes. Please arrive fifteen minutes early so the instructor can ask about your experience and explain the pool rules.""",[
(5,'Who is the confidence class intended for?',['Experienced racing swimmers.','People who have never entered water.','Children learning basic safety.','Adults with some swimming ability.'],'D','not complete beginners；有一点基础但缺乏信心的成人。'),
(6,'Why does the woman prefer Saturday?',['The group is larger.','She can attend the entire lesson.','The water is shallower.','The instructor charges less.'],'B','周四下班后会迟到，周六可完整参与。'),
(7,'What happens to the trial payment if she joins?',['It counts towards the course fee.','It pays for a swimming cap.','It is given to the instructor.','It covers an extra session.'],'A','deduct that amount from the course fee，试课费抵课程费。'),
(8,'Why should she arrive early for the trial?',['To purchase equipment.','To help prepare the pool.','To discuss her experience with the instructor.','To meet the children in Tuesday\'s class.'],'C','早到供教练了解经历并讲解规则。')])
section('听力 A · 9—12','listenA',"""M: We're joined by travel writer Helen Price. Helen, your latest book is about journeys close to home. Why choose that subject?
W: During a period when I couldn't travel far, I started taking local buses to the end of their routes. I discovered places I'd ignored for years because they seemed too ordinary.
M: Did you plan each trip carefully?
W: I checked the last bus home, but otherwise left the day fairly open. Once I spent an hour talking to a man who restored old furniture. That conversation would never have happened if I'd been rushing through a list of attractions.
M: Some readers might worry about wasting a day.
W: An uncertain result isn't necessarily a waste. You may learn what doesn't interest you. Of course, I don't suggest wandering without thinking about safety or transport.
M: Is the book mainly a collection of recommended destinations?
W: There are places in it, but I hope readers borrow the approach rather than repeat my exact routes. Ask a question, follow a small interest, and allow time for something unexpected.
M: What are you working on next?
W: A series of interviews with bus drivers. They see their towns changing day by day, yet travellers rarely ask them what they've noticed.""",[
(9,'How did Helen begin exploring nearby places?',['She joined a furniture business.','She rode buses to their final stops.','She followed a guidebook overseas.','She accepted a job as a driver.'],'B','taking local buses to the end of their routes。'),
(10,'What did Helen always check before a trip?',['The cost of every attraction.','The weather in other towns.','The time of the final return bus.','The names of local writers.'],'C','checked the last bus home。'),
(11,'What does Helen hope readers will do?',['Adopt her way of exploring.','Visit every place in her book.','Avoid all advance planning.','Interview furniture makers only.'],'A','borrow the approach rather than repeat exact routes。'),
(12,'Why is Helen interested in bus drivers?',['They can arrange free journeys.','They usually write detailed diaries.','They know the safest overseas routes.','They observe changes in local places.'],'D','see their towns changing day by day。')])
section('听力 A · 13—16','listenA',"""When our sports club bought an online booking system, we thought the main advantage would be less paperwork. Members could reserve a court from home, and volunteers would no longer need to answer calls all evening. Those benefits appeared quickly, but another problem became visible. Several members booked the same popular evening slots every week, then cancelled just before the session began. Other people had already made different plans, so the courts remained empty despite strong demand. Charging a cancellation fee seemed an obvious answer, but the committee was concerned about genuine emergencies. Instead, we introduced a waiting list and asked members to cancel at least four hours ahead whenever possible. People on the list now receive a message as soon as a place becomes available. We also limit advance bookings to two per member each week. Anyone can book an additional session on the day if a court is free. The changes have reduced empty slots without preventing regular players from organising their week. We still accept telephone bookings from members who cannot use the website. Technology has helped us see the pattern, but it was a decision about fairness, not a new piece of software, that made better use of the courts possible.""",[
(13,'What benefit did the club originally expect?',['Less administrative work.','More professional players.','Lower electricity bills.','Longer opening hours.'],'A','main advantage less paperwork，减少电话与手工预约。'),
(14,'Why were some popular slots left unused?',['The website displayed incorrect times.','Players could not find the courts.','Volunteers forgot to open the doors.','Members cancelled too late.'],'D','临近开场才取消，别人已另作安排。'),
(15,'How many advance sessions may a member book weekly?',['One.','Two.','Three.','Four.'],'B','limit advance bookings to two；当日空场可另约。'),
(16,'What does the speaker emphasise at the end?',['Telephone bookings should end soon.','Software can replace all volunteers.','Fair rules are needed alongside technology.','Regular players should receive priority.'],'C','技术揭示问题，公平规则才改善利用率。')])
section('听力 A · 17—20','listenA',"""I used to think travelling light meant being prepared for nothing. Before every weekend away, I packed a spare pair of shoes, several books and clothes for weather that rarely arrived. My bag was always the heaviest, although I usually wore the same two outfits. Then a friend invited me on a walking holiday. We would carry everything ourselves, and she suggested weighing each item before deciding whether to bring it. At first I found this rather extreme. But seeing the numbers changed my mind. My three books weighed more than my waterproof jacket and lunch together. I chose one small book and left the others behind. I also realised that two shirts could be washed during the trip instead of packing one for every day. The holiday was not perfect. I missed my comfortable slippers on the first evening, and I borrowed a pen from another walker. Neither problem spoiled the experience. By the third day, I hardly noticed my bag. I am not trying to own as few things as possible now. I simply ask whether an object is useful enough to carry. That question has made travelling easier and has even changed what I keep on my desk at home.""",[
(17,'What was the speaker\'s former packing habit?',['Borrowing everything from friends.','Carrying many unnecessary items.','Avoiding all spare clothing.','Taking only a waterproof jacket.'],'B','为罕见情况多带东西，常只穿两套。'),
(18,'What persuaded the speaker to pack less?',['Losing a bag at a station.','Paying an airline fee.','Reading a travel advertisement.','Comparing the weight of items.'],'D','称重后数字改变了想法。'),
(19,'How did the missing items affect the holiday?',['They forced the speaker to return home.','They caused serious arguments.','They created only minor difficulties.','They made walking impossible.'],'C','想拖鞋、借笔，但 neither problem spoiled experience。'),
(20,'What principle does the speaker now follow?',['Consider whether an item is worth carrying.','Keep the smallest possible number of objects.','Buy new equipment before every trip.','Pack exactly the same things as friends.'],'A','判断物品是否有用到值得携带，不是极端少物。')])
section('听力 B · 21—25','listenB',"""Here is some information for people joining Sunday's coastal walk. We will meet outside the station at nine thirty, not at the harbour as originally advertised. Roadworks have made the harbour meeting point difficult to reach. The walk is twelve kilometres long and includes a short climb, so please wear comfortable boots. Trainers may be slippery if the path is wet. Bring your own lunch because the cafe halfway along the route is closed for the season. We will provide drinking water at the starting point, but you need a bottle to carry it in. Our guide, Rachel, has worked in the area for seven years and knows a great deal about local birds. She will bring a telescope for everyone to share. Please leave dogs at home on this particular walk, as we will pass through a protected nesting area. We expect to finish at around three, although the exact time will depend on the weather and the pace of the group. If strong winds force us to cancel, we will send a text message by eight on Sunday morning. Make sure the phone number on your booking is correct. You do not need to call us unless your plans change.""",[
(21,'Meeting place: outside the ____',None,'station','改在车站外集合，harbour是原地点。'),
(22,'Length of the walk: ____ kilometres',None,'12|twelve','twelve kilometres，路线长度。'),
(23,'Recommended footwear: ____',None,'boots','wear comfortable boots；trainers湿滑。'),
(24,'Equipment the guide will share: a ____',None,'telescope','guide will bring a telescope。'),
(25,'Cancellation message sent by ____ in the morning',None,'8|eight','八点前发取消短信，九点半为集合时间。')])
section('阅读 A · 26—30','readA',"""When a railway company invited passengers to comment on a station improvement plan, most of the proposals concerned speed. There would be faster ticket machines, wider gates and a shorter route between platforms. These changes were welcome, but a group of older passengers noticed something missing: places to sit.

The designers had assumed that passengers wanted to spend as little time in the station as possible. For someone changing trains, however, waiting was unavoidable. A retired teacher explained that she sometimes stood for twenty minutes because the few existing seats were occupied. She could manage the journey itself, but the uncertainty about resting made her reluctant to travel alone.

In response, the company installed temporary benches and observed how they were used. Some were placed directly beside the platforms; others were in a quieter area near the ticket office. Surprisingly, the quieter seats were often preferred, even though passengers had to walk slightly farther to reach their trains. Clear information screens allowed them to wait comfortably without worrying about missing an announcement.

The trial also revealed that seat design mattered. Very low benches were difficult for some people to get up from. Seats without armrests offered little support. The company therefore ordered a mixture of seating rather than choosing one style for the whole station. Space beside the benches was left clear for wheelchairs and luggage.

None of this removed the need for efficient ticket machines or accessible platforms. It widened the meaning of a successful journey. A station could move people quickly and still make them feel anxious or exhausted. Equally, adding seats without providing reliable travel information would not solve the problem.

The passengers who raised the issue were not asking the company to make travel slower. They were asking it to recognise that different people move at different speeds. Listening to them helped produce a station that was easier to use for families with young children, travellers carrying heavy bags and many others who had never thought of themselves as needing special assistance.""",[
(26,'What did the older passengers think the plan lacked?',['Additional ticket machines.','A way to buy cheaper tickets.','Suitable places to rest.','A shorter railway route.'],'C','首段 places to sit 是被忽略的需求。'),
(27,'Why was the retired teacher hesitant to travel alone?',['She was unsure whether she could sit while waiting.','She could not understand train timetables.','She disliked all ticket machines.','She could not walk between platforms.'],'A','uncertainty about resting；并非不能完成旅行本身。'),
(28,'What made the quieter seating area practical?',['Staff collected passengers\' luggage.','Information screens kept passengers informed.','Trains stopped beside the ticket office.','Announcements were no longer necessary.'],'B','清晰信息屏让人安心等候，不怕错过信息。'),
(29,'Why did the company choose different kinds of seats?',['To match the colours of the trains.','To make the station look more expensive.','To reduce the total number of benches.','To meet different physical needs.'],'D','座位高度、扶手适应不同身体需求。'),
(30,'What is the main lesson of the project?',['Older travellers prefer slow trains.','Efficient machines can replace passenger advice.','Station design should accommodate varied users.','Special assistance should be limited to families.'],'C','最后强调不同人的节奏和需求，改善使更多人受益。')])
section('阅读 A · 31—35','readA',"""A language teacher asked her adult students to keep a record of the English they encountered outside class. She expected lists of news programmes, films and books. Instead, many records contained short messages: a delivery notice, an instruction on a machine, a conversation with a visitor. These encounters lasted only a few seconds, but they mattered because the students needed to do something with the information.

One student, Karim, described reading the same message on a coffee machine every morning. For weeks he had understood only that something was wrong. One day he looked closely and learned that the water container needed filling. The words became memorable because they solved an immediate problem. He was not simply collecting vocabulary for a future test.

The teacher began using these examples in class. Students brought photographs or wrote down phrases they remembered. Together they discussed what the speaker or writer was trying to achieve. Sometimes they discovered that understanding every word was unnecessary. A familiar symbol, the location of a message or the action of another person could help establish the meaning.

This did not mean that formal study had become useless. Students still needed grammar, vocabulary and opportunities to practise. Everyday encounters were often too brief to explain why a particular expression worked. The classroom gave them time to examine patterns and ask questions that would be inconvenient in the middle of a transaction.

Over several months, the students became more willing to notice English around them. They also began distinguishing between an expression they could recognise and one they could confidently use themselves. Seeing a phrase once did not make it part of their active vocabulary. Returning to it in different situations helped.

The project offered a modest lesson: useful learning material is not always labelled as educational. A machine's instruction may be less exciting than a novel, but for a learner who needs a cup of coffee, it has an obvious purpose. Connecting classroom work with such purposes can make practice feel less separate from ordinary life.""",[
(31,'What surprised the teacher about the students\' records?',['They contained many brief practical messages.','They focused entirely on films.','They included no examples of English.','They were written by visitors.'],'A','预想新闻影视书籍，实际多是短实用信息。'),
(32,'Why did Karim remember the words on the machine?',['They appeared in a textbook.','They were repeated by his teacher.','They were unusually difficult.','They helped him solve a current problem.'],'D','知道该加水，词与眼前实际用途建立联系。'),
(33,'What did classroom discussion show?',['Symbols always replace language.','Context can help people understand a message.','Short messages contain no grammar.','Every word must be translated first.'],'B','第三段符号、位置、他人行动构成语境线索。'),
(34,'How did formal lessons support everyday learning?',['They removed all need for practice.','They limited students to written English.','They provided time to examine language patterns.','They prevented students from making transactions.'],'C','课堂容许分析规律并提问，现实短暂接触未必能解释。'),
(35,'What does the writer suggest about learning materials?',['Only books develop active vocabulary.','Practical messages are always better than novels.','Educational labels guarantee effective learning.','Ordinary situations can provide valuable examples.'],'D','末段 useful material not always labelled educational。')])
section('阅读 A · 36—40','readA',"""A hotel beside a national park once encouraged guests to visit the same famous viewpoint at sunrise. The photograph in its brochure showed an empty path and a peaceful valley. In reality, visitors often found a crowd. Some arrived so early that they disturbed nearby residents, while others left disappointed because the experience did not match the picture.

The hotel manager could have removed the photograph and continued recommending the place. Instead, she asked a local guide to help guests understand the wider area. The guide suggested several less familiar walks, each with a different feature: old trees, a riverside path or an easy route suitable for children. None was presented as a secret place that everyone had to see.

Staff also changed the questions they asked. Rather than beginning with a list of popular attractions, they asked guests how much time they had, how far they wanted to walk and what interested them. A visitor hoping to draw plants received different advice from a family wanting a short outdoor break. The famous viewpoint remained an option, but it was no longer treated as the only meaningful destination.

Some guests still requested the sunrise visit. For them, staff explained the likely crowds and suggested travelling quietly and staying on marked paths. Giving realistic information did not necessarily discourage visits. It helped people make a choice based on what they valued rather than what a photograph seemed to promise.

The change brought no dramatic increase in room bookings, and the manager did not claim that it had solved the park's crowding problem. Its effect was smaller and more local. Guests reported feeling better prepared, and a few businesses away from the busiest road received additional visitors.

Tourism advice often turns a place into a checklist: arrive, take the expected photograph, move on. This hotel tried to replace that checklist with a conversation. The lesson is not that famous places should be avoided. It is that a good recommendation connects a person's interests with the reality of a place, including its limitations.""",[
(36,'Why were some visitors disappointed at the viewpoint?',['It was no longer inside the park.','It was much busier than the brochure suggested.','The path had been permanently closed.','Sunrise could not be seen from it.'],'B','画面空静而现实拥挤，预期落差。'),
(37,'How were the alternative walks presented?',['As routes that every guest must complete.','As secret locations unavailable to residents.','As places with different features to suit visitors.','As replacements for all guided tours.'],'C','每条各有特色，无必须打卡的暗示。'),
(38,'What became the starting point for staff recommendations?',['Guests\' interests and practical circumstances.','The number of photographs guests owned.','The price of nearby hotel rooms.','The guide\'s favourite social-media accounts.'],'A','先问时间、行走距离和兴趣。'),
(39,'What result does the manager claim?',['A major increase in room bookings.','An end to crowding across the park.','The disappearance of sunrise visits.','Better-prepared guests and some local benefits.'],'D','倒数第二段限定为较小、局部改善。'),
(40,'Which statement best reflects the writer\'s view?',['Famous destinations should be excluded from travel plans.','Recommendations should connect people with realistic choices.','Brochure photographs are the only useful travel information.','All tourists want the same type of experience.'],'B','末段核心：个人兴趣与地点现实，包括局限，相匹配。')])
section('阅读 B · 41—45','readB',"""Five people discuss learning a new skill as an adult.

Marta: I joined a drawing class after years of saying I had no talent. The useful part was seeing the teacher make corrections to her own sketch. Until then, I had imagined that skilled people produced perfect work immediately. Watching her change a line made my mistakes feel normal. I still have much to learn, but I no longer see a poor first attempt as evidence that I should stop.

Owen: My guitar stayed in its case when I planned to practise for an hour every Sunday. Something always interrupted the plan. Now I leave it beside my chair and play for ten minutes after dinner. I have made more progress with these small regular sessions than with ambitious promises. A routine that fits my life is more useful than one that looks impressive on paper.

Priya: I tried learning to repair my bicycle entirely from videos. They were helpful, but I could not always tell whether I was holding a tool correctly. One afternoon with an experienced neighbour cleared up several problems. Independent learning is valuable, yet there are moments when another person can notice a small error before it becomes a lasting habit. Asking for help does not mean you have failed.

Simon: People keep asking whether my photography course will help me earn money. That question misses the reason I enrolled. I enjoy looking carefully at ordinary things, and the course gives me a reason to go outside. A new skill can improve your life without becoming a business. I would rather protect that pleasure than turn every weekend into a search for customers.

Tessa: In my first language class, I compared myself with someone who seemed to understand everything. Later I discovered that she had studied the language at school for six years. We were not starting from the same point. I now compare my work with what I could do last month. Other learners can encourage me, but their speed is not a fair measure of my progress.""",[])
opts=['Short, frequent practice can be effective.','Previous experience makes comparisons unfair.','A skill must produce an income.','Expert corrections can support independent learning.','Mistakes are a normal part of developing a skill.','Learning can be worthwhile for personal enjoyment.','Adults should avoid difficult new activities.']
sections[-1]['questions']=[q(n,name,opts,key,why) for n,name,key,why in [(41,'Marta','E','教师也修改作品，让她认识到犯错正常。'),(42,'Owen','A','每日十分钟比每周宏大计划更可持续。'),(43,'Priya','D','邻居及时看出动作错误，补充视频自学。'),(44,'Simon','F','摄影为兴趣与生活体验，不必变生意。'),(45,'Tessa','B','同学有六年基础，不能以她速度衡量自己。')]]
section('阅读 C · 46—55','readC',"""A walking map can help visitors explore a town without depending on a car. However, a useful map must do more than [46] the names of streets. It should show safe crossings, public toilets and places where people can [47]. These details are especially important for families and older visitors.

When a local group produced its first map, members asked residents to test the routes. Their [48] revealed several problems. One path looked short on paper but included a steep hill. Another passed through a gate that was often [49]. The group changed the routes instead of expecting visitors to manage these difficulties alone.

The finished map uses clear symbols and [50] descriptions. Distances are given in both metres and approximate walking time. Since people move at different speeds, the times are intended as a [51], not a promise. A note encourages walkers to allow extra time for breaks.

Copies are [52] at the station and local shops. An online version is updated when a road closes, but the printed map remains useful for people without a phone. Volunteers [53] the routes twice a year to check for changes. This regular work helps keep the information [54]. The project shows that good visitor information depends on understanding real journeys, rather than simply producing an [55] design.""",[])
opts=['rest','available','accurate','feedback','list','inspect','simple','locked','guide','attractive','suddenly','refuse','distance','narrow','disappear']
answers=['E','A','D','H','G','I','B','F','C','J'];reasons=['list street names，列出街名。','places where people can rest，能休息的地方。','their feedback revealed problems，反馈揭示问题。','gate was often locked，门常锁。','clear symbols and simple descriptions，简明说明。','a guide, not a promise，指导参考非保证。','copies are available，地图可领取。','inspect routes，定期检查路线。','keep information accurate，保持信息准确。','an attractive design，漂亮的设计并不够。']
sections[-1]['questions']=[q(46+i,str(46+i),opts,answers[i],reasons[i]) for i in range(10)]
sections.append({'title':'写作 · 56','kind':'writing','chart':{'title':'某社区居民每周步行锻炼次数','labels':['2021','2022','2023','2024','2025'],'values':[2,2.4,2.8,3.3,3.8],'unit':'次'},'questions':[q(56,'Write an essay of about 120 words based on the chart. Describe and interpret the chart briefly, and give your comments.',None,'','描述每周次数从2次增至3.8次的上升趋势，再评论步行的可行性及社区提供安全路线的作用。避免把次数写成人数。')],'model':"The chart presents the average number of times residents in a community walked for exercise each week between 2021 and 2025. The figure increased from two to 3.8, showing a steady rise in this activity. In my view, walking is a useful way to include exercise in everyday life. It requires little equipment and can be done with friends or family members. However, encouraging people to walk also means providing a suitable environment. Safe crossings, comfortable paths and places to rest can make a difference, especially for older residents. The community should continue improving these facilities and organise activities that welcome beginners. Small, regular changes may help more people develop an active lifestyle over time."})
Path(__file__).with_name('paper02.json').write_text(json.dumps({'id':2,'title':'出行与学习','sections':sections},ensure_ascii=False,indent=2),encoding='utf-8')
