# 数据结构

import arrow
from enum import Enum

#资源库
class QuestionBank:
    '''
    题库属性
    '''
    def __init__(self,name=None,title=None,description=None,countOfJustQuestion=None,
                 countOfTopQuestion=None,countOfBotQuestion=None,ctime=None,creator=None):
        '''
        :param name: 名称,可区分
        :param title: 标题
        :param description: 描述
        :param countOfJustQuestion: 正题的数量
        :param countOfTopQuestion: 正题或超题的数量
        :param countOfBotQuestion: 最底层题的数量
        :param ctime: 创建时间
        :param creator: 创建人
        '''
        self.name = name
        self.title = title
        self.description = description
        self.countOfJustQuestion = countOfJustQuestion
        self.countOfTopQuestion = countOfTopQuestion
        self.countOfBotQuestion = countOfBotQuestion
        self.ctime = arrow.now().format('YYYY-MM-DDTHH:mm:dd')
        self.creator = creator


class QuestionContentPartype:
    '''
    题目内容(偏型)
    '''
    def __init__(self,contOfQuery=None,contOfAnalysis=None,contOfScantron=None,contOfKey=None):
        '''

        :param contOfQuery: 题目内容,html,word,latex 片段
        :param contOfAnalysis: 题目解析
        :param contOfScantron: 答辅区域
        :param contOfKey: 参考答案
        '''
        self.contOfQuery = contOfQuery
        self.contOfAnalysis = contOfAnalysis
        self.contOfScantron = contOfScantron
        self.contOfKey = contOfKey


class QuestionStructurePartype:
    def __init__(self,BurtreeNode=None):
        self.BurtreeNode = BurtreeNode


class QuestionCheckPartype:
    '''
    题目审查
    '''
    def __init__(self,statusOfCheck='open'):
        self.statusOfCheck = statusOfCheck

    def getstatus(self):
        return self.statusOfCheck

    def setstatus(self,statusOfCheck):
        self.statusOfCheck = statusOfCheck


class QuestionSourcePartype:
    def __init__(self):
        pass


class QuestionDisciplinePartype:
    '''
    科目偏型
    '''
    def __init__(self,title=None,appliedTo=None,description=None):
        '''

        :param title: 科目偏型
        :param appliedTo: Question
        :param description: 英语题的进一步类型定义
        '''
        self.title = title
        self.appliedTo = appliedTo
        self.description = description


class QuestionFoSelect(QuestionDisciplinePartype):
    '''
    选择题辅型
    '''
    def __init__(self,optionCount=4,optionOrdinal='a',optionMultiplicity=1):
        '''

        :param optionCount: 选项个数
        :param optionOrdinal: 选项的序数词1,a,A
        :param optionMultiplicity: 正确答案的个数
        '''
        super().__init__()
        self.optionCount = optionCount
        self.optionOrdinal = optionOrdinal
        self.optionMultiplicity = optionMultiplicity


class QuestionFoFillin(QuestionDisciplinePartype):
    '''
    填空题辅型
    '''
    def __init__(self,blankCount=1,blankLengths=5):
        '''

        :param blankCount: 空白个数
        :param blankLengths: 空白长度
        '''
        super().__init__()
        self.blankCount = blankCount
        self.blankLengths = blankLengths


class QuestionFoWriteout(QuestionDisciplinePartype):
    '''
    作答题辅型
    '''
    def __init__(self,size=None):
        '''

        :param size: 作答区尺寸
        '''
        super().__init__()
        self.size = size


class QuestionFoEnglish(QuestionDisciplinePartype):
    '''
    作文辅型
    '''
    def __init__(self):
        super().__init__()


class QuestionFoEnglishSimpleSelection:
    pass


class QuestionFoEnglishReadingComprehension:
    pass


class QuestionFoEnglishMatching:
    pass


class QuestionFoEnglishCloze:
    pass


class QuestionFoEnglishReadWriteTask:
    pass


class QuestionFoEnglishFillWordInText:
    pass


class QuestionFoEnglishFillWordInSentence:
    pass


class QuestionFoEnglishTextCorrection:
    pass


class QuestionFoEnglishSentenceCorrection:
    pass


class QuestionFoEnglishPatternTransformation:
    pass


class QuestionFoEnglishPhraseTranslation:
    pass


class QuestionFoEnglishSentenceTranslation:
    pass


class QuestionFoEnglishSentenceCompletion:
    pass


class QuestionFoMath:
    pass


class QuestionDifficultyKind(Enum):
    '''
    难易程度
    '''
    容易 = 1
    较易 = 2
    中 = 3
    较难 = 4
    难 = 5


class QuestionDisciplineKind(Enum):
    '''
    学科内容
    '''
    chinese = 1
    english = 2
    math = 3
    physics = 4
    chemistry = 5
    biology = 6
    politics = 7
    history = 8
    geography = 9
    physical = 10
    music = 11


class QuestionComboObjectiveKind:
    pass


class QuestionEnglishComboObjectiveKind:
    '''
    考点
    '''
    词汇 = 1
    语法 = 2


class QuestionMaterialKind(Enum):
    '''
    材料类型
    '''
    广告通知类 = 1
    叙事类 = 2
    说明议论类 = 3
    对话类 = 4
    说明文 = 5
    记叙文 = 6
    议论文 = 7
    夹叙夹议 = 8


class QuestionMaterialLengthDeg(Enum):
    '''
    材料长度
    '''
    短 = 1
    中 = 2
    中长 = 3
    长 = 4


class EnglishQuestionComboFormatKind(Enum):
    '''
    (英语)作答形式
    '''
    SimpleSelection = 1
    ReadingComprehension = 2
    Matching = 3
    Cloze = 4
    ReadWriteTask = 5
    FillWordInText = 6
    FillWordInSentence = 7
    TextCorrection = 8
    SentenceCorrection = 9
    PatternTransformation = 10
    PhraseTranslation = 11
    SentenceTranslation = 12
    SentenceCompletion = 13


class QuestionQueryFormatKind(Enum):
    '''
    问询形式: 暂不用
    '''
    listen = 1
    watch = 2
    read = 3


class QuestionResponseFormatKind(Enum):
    '''
    答题类型
    '''
    select = 1
    fillin = 2
    writeout = 3
    compose = 4


class QuestionSourceLocaEnum(Enum):
    '''
    题目来源地
    '''
    全国1卷 = 1
    江苏1卷 = 2


class QuestionSourceKind(Enum):
    '''
    题目来源:高考真题，同步练习，复习模拟
    '''
    FromPast = 1
    FromExercise = 2
    FromSimulation = 3


class BurTreeNode:
    def __init__(self,**kw):
        self.outerlyr = kw.get('outerlyr')
        self.innerlyr = kw.get('innerlyr')
        self.plydad = kw.get('plydad')
        self.plyson = kw.get('plyson')
        self.dadinner = kw.get('dadinner')
        self.leastdaderninner = kw.get('leastdaderninner')
        self.mostdaderninner = kw.get('mostdaderninner')
        self.mostdadwardinner = kw.get('mostdadwardinner')
        self.mostdaderninnersuper = kw.get('mostdaderninnersuper')
        self.mostdadwardinnersuper = kw.get('mostdadwardinnersuper')
        self.daderninnerjust = kw.get('daderninnerjust')
        self.dadouter = kw.get('dadouter')
        self.leastdadernouter = kw.get('leastdadernouter')
        self.mostdadernouter = kw.get('mostdadernouter')
        self.dadernouterjust = kw.get('dadernouterjust')
        self.dadwardouterjust = kw.get('dadwardouterjust')
        self.soninner = kw.get('soninner')
        self.sonernjust = kw.get('sonernjust')
        self.sonernsub = kw.get('sonernsub')
        self.sonouter = kw.get('sonouter')
        self.leastsonernouter = kw.get('leastsonernouter')
        self.sonerncxlyrojust = kw.get('sonerncxlyrojust')
        self.mostsonerncrslyro = kw.get('mostsonerncrslyro')
        self.dadernlyroxxx = kw.get('dadernlyroxxx')
        self.dadernlyroxxxjust = kw.get('dadernlyroxxxjust')
        self.dadwardlyroxxxjust = kw.get('dadwardlyroxxxjust')
        self.mostdadwardlyroxxxjust = kw.get('mostdadwardlyroxxxjust')
        self.leastsonernlyroxxx = kw.get('leastsonernlyroxxx')
        self.sonernsmlyrojust = kw.get('sonernsmlyrojust')
        self.sonwardxxlyrojust = kw.get('sonwardxxlyrojust')
        self.mostsonwardxxlyro = kw.get('mostsonwardxxlyro')


#知识体
class BokT(BurTreeNode):
    '''
    知识体树
    '''
    def __init__(self,**kw):
        self.root = kw.get('root')
        super().__init__(**kw)


class BokN:
    '''
    知识体树节点
    '''
    def __int__(self,burTreeNode,kind):
        self.burTreeNode = burTreeNode
        self.kind = kind


#教材体
class BotT(BurTreeNode):
    def __init__(self,**kw):
        self.root = kw.get('root')
        super().__init__(**kw)


class Botn:
    def __init__(self,burTreeNode,kind):
        self.burTreeNode = burTreeNode
        self.kind = kind

