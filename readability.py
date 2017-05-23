#!/usr/bin/env python

import math

from utils import get_char_count
from utils import get_words
from utils import get_sentences
from utils import count_syllables
from utils import count_complex_words


class Readability:
    analyzedVars = {}

    def __init__(self, text):
        self.analyze_text(text)

    def analyze_text(self, text):
        words = get_words(text)
        char_count = get_char_count(words)
        word_count = len(words)
        sentence_count = len(get_sentences(text))
        syllable_count = count_syllables(words)
        complexwords_count = count_complex_words(text)
        avg_words_p_sentence = word_count/sentence_count

        self.analyzedVars = {
            'words': words,
            'char_cnt': float(char_count),
            'word_cnt': float(word_count),
            'sentence_cnt': float(sentence_count),
            'syllable_cnt': float(syllable_count),
            'complex_word_cnt': float(complexwords_count),
            'avg_words_p_sentence': float(avg_words_p_sentence)
        }

        outData = {
            'char_cnt': float(char_count),
            'word_cnt': float(word_count),
            'sentence_cnt': float(sentence_count),
            'syllable_cnt': float(syllable_count),
            'complex_word_cnt': float(complexwords_count),
            'avg_words_p_sentence': float(avg_words_p_sentence)
        }
        return outData


    def ARI(self):
        score = 0.0
        if self.analyzedVars['word_cnt'] > 0.0:
            score = 4.71 * (self.analyzedVars['char_cnt'] / self.analyzedVars['word_cnt']) + 0.5 * (self.analyzedVars['word_cnt'] / self.analyzedVars['sentence_cnt']) - 21.43
        return score

    def FleschReadingEase(self):
        score = 0.0
        if self.analyzedVars['word_cnt'] > 0.0:
            score = 206.835 - (1.015 * (self.analyzedVars['avg_words_p_sentence'])) - (84.6 * (self.analyzedVars['syllable_cnt']/ self.analyzedVars['word_cnt']))
        return round(score, 4)

    def FleschKincaidGradeLevel(self):
        score = 0.0
        if self.analyzedVars['word_cnt'] > 0.0:
            score = 0.39 * (self.analyzedVars['avg_words_p_sentence']) + 11.8 * (self.analyzedVars['syllable_cnt']/ self.analyzedVars['word_cnt']) - 15.59
        return round(score, 4)

    def GunningFogIndex(self):
        score = 0.0
        if self.analyzedVars['word_cnt'] > 0.0:
            score = 0.4 * ((self.analyzedVars['avg_words_p_sentence']) + (100 * (self.analyzedVars['complex_word_cnt']/self.analyzedVars['word_cnt'])))
        return round(score, 4)

    def SMOGIndex(self):
        score = 0.0
        if self.analyzedVars['word_cnt'] > 0.0:
            score = (math.sqrt(self.analyzedVars['complex_word_cnt']*(30/self.analyzedVars['sentence_cnt'])) + 3)
        return score

    def ColemanLiauIndex(self):
        score = 0.0
        if self.analyzedVars['word_cnt'] > 0.0:
            score = (5.89*(self.analyzedVars['char_cnt']/self.analyzedVars['word_cnt']))-(30*(self.analyzedVars['sentence_cnt']/self.analyzedVars['word_cnt']))-15.8
        return round(score, 4)

    def LIX(self):
        longwords = 0.0
        score = 0.0
        if self.analyzedVars['word_cnt'] > 0.0:
            for word in self.analyzedVars['words']:
                if len(word) >= 7:
                    longwords += 1.0
            score = self.analyzedVars['word_cnt'] / self.analyzedVars['sentence_cnt'] + float(100 * longwords) / self.analyzedVars['word_cnt']
        return score

    def RIX(self):
        longwords = 0.0
        score = 0.0
        if self.analyzedVars['word_cnt'] > 0.0:
            for word in self.analyzedVars['words']:
                if len(word) >= 7:
                    longwords += 1.0
            score = longwords / self.analyzedVars['sentence_cnt']
        return score


if __name__ == "__main__":
    text = """SAP CEO Bill McDermott:  Empathy to Action Is a Race Without a Finish Line. During his keynote to 30,000 live attendees at the companys annual SAPPHIRE NOW event, SAP CEO Bill McDermott wasted no time checking off a list of impressive accomplishments and just as quickly proved that his empathy to action mantra from a year ago was not an empty promise. And with a visit from Michael Dell and news about SAP Leonardo, the companys biggest bet since SAP HANA, McDermott made a very strong argument that even though SAP has been an IT innovator for over 40 years, the company is still hungry for more. Weve been turning empathy into action at SAP, said McDermott. You wanted detailed, solution road maps, we gave them to you. SAP also provided SAP Transformation Navigator, to help customers plan a smooth transition to SAP S/4 HANA, the in-memory ERP suite available on premise or in the cloud. SAP has also been busy enhancing the user experience for its customers by strengthening its portfolio with SAP Fiori. Empathy to action is a race without a finish line, said McDermott who had no problem addressing the issue of indirect access, which is causing some anxiety for customers. Protecting IP and accommodating the ease of doing business is a delicate balance. But even as we maintain that balance we can still show greater empathy for you. As a result, a new Simplified Pricing model was announced whereby Procure to Pay and Order to Cash scenarios are based on actual orders. In addition, static read access in third-party systems is owned by the customer. This is another example where if we listen we can evolve and improve, said McDermott. SAP will remain a culture in the pursuit of excellence. We understand you, and you alone determine whether we win or lose. McDermott said SAP has always been known as a humble company but its hunger to help customers succeed is insatiable. For 45 years SAP has co-innovated together with its customers, providing SAP MaxAttention, to protect their investments, while accelerating its innovation strategy since 2010. We have invested more than 50 billion in innovation to drive your business forward, said McDermott. SAP HANA has become the de facto, standard in-memory platform for the enterprise. SAP HANA was adopted faster by the global SAP customer base than any other SAP product. And with SAP S/4HANA the company is well-positioned to provide Cloud ERP for the 21st century. Its the most intelligent, relevant cloud ERP in the marketplace today, said McDermott. Were proud to be supported by fastest ecosystem in terms of growth year over year in the industry. SAP partners now include Apple, Google, and Facebook. Cutting out the Corporate Cholesterol We want to focus on what matters and cut out the corporate cholesterol, said McDermott. We want healthy companies to lead the way as best run businesses. MOD Pizza, for instance, is growing very quickly thanks to SAP S/4 HANA Cloud. Mai Jim is reinventing customer experience with SAP Hybris. Jaguar is inspiring its workforce with SAP SuccessFactors. JP Morgan Chase is boosting transparency and compliance with SAP Ariba. From this position of enormous strength, we are ready to join hands with you, to seize the future, said McDermott. For Whom the Dell Tolls another important customer that is using SAP to transform its business is Dell and none other than founder CEO Michael Dell was on hand to let the SAPPHIRE NOW audience know where the IT industry is headed. Dell said the cost of making something intelligent is fast approaching zero dollars, seeing explosive growth of all things intelligent across all sectors and industries. When you get all this data coming in from hundreds of billions of connected devices and apply to that artificial intelligence, its almost like a fourth industrial revolution and an incredible opportunity for companies to re-imagine themselves in this digital age. Dell has recently made bold moves with recent acquisitions, bundled into a new group called Dell Technologies, and is using SAP HANA to help manage this new venture. SAP is helping us run the business in real time whether finance, procurement, supply chain, or travel expenses, said Dell. Its helping us deliver great capabilities to our customers. Dell also said digital transformation is not an IT project but a CEO project. If your CEO doesnt understand that, have him call me, quipped Dell. It has to be driven by the CEO and the IT organization must be completely aligned with strategy of the company. Competing in the Era of Digital Business with so many new buzzwords like blockchain, machine learning and artificial intelligence vying for peoples attention, few can explain what all of it actually means. From SAPs perspective, its all about intelligently connecting things, people and businesses with speed as the key to digital business success. If we do it right, you can know more, do more and care more for your customers, said McDemrott. In response, SAP Leonardo SAPs biggest move since SAP HANA, according to McDermott will help SAP customers compete in the digital business era. SAP Leonardo is a digital innovation system that integrates breakthrough technologies and runs them seamlessly in the cloud. It also offers design thinking methodology and SAP expertise to help customers rapidly adopt new capabilities and business models and remain on the cutting edge as SAP adds new technologies to the portfolio. It is SAPs job to be an early adopter of the intelligent enterprise, said McDemott. We want you to win."""

    rd = Readability(text)
    print('Test text:')
    print('"%s"\n' % text)
    print('ARI: ', rd.ARI())
    print('FleschReadingEase: ', rd.FleschReadingEase())
    print('FleschKincaidGradeLevel: ', rd.FleschKincaidGradeLevel())
    print('GunningFogIndex: ', rd.GunningFogIndex())
    print('SMOGIndex: ', rd.SMOGIndex())
    print('ColemanLiauIndex: ', rd.ColemanLiauIndex())
    print('LIX: ', rd.LIX())
    print('RIX: ', rd.RIX())
    print('Analysis of Text', rd.analyze_text(text))
