#!/usr/bin/python
# -*- coding: utf-8 -*-

import re

from utils.Parsers import chapter_paragraph_parser


class CDR:
    __CHPTRMAX = {
        1: 9,
        2: 7,
        3: 9,
        4: 9}

    __text = {
        1: {
            0: "**FIRST HEAD OF DOCTRINE**\n\n>**Of Divine Predestination**",
            1: ("*That the will of God to save those who would believe and would persevere in faith and in the "
                "obedience of faith, is the whole and entire decree of election unto salvation, and that nothing else "
                "concerning this decree has been revealed in God's Word.*\n\n>For these deceive the simple and "
                "plainly contradict the Scriptures which declare that God will not only save those who will believe, "
                "but that He has also from eternity chosen certain particular persons to whom above others He in time "
                "will grant both faith in Christ and perseverance, as it is written: \"I have manifested Thy Name "
                "unto the men which Thou gavest Me out of the world\" (John 17:6). \"And as many as were ordained to "
                "eternal life believed\" (Acts 13:48). And: \"According as He hath chosen us in Him before the "
                "foundation of the world, that we should be holy and without blame before Him in love\" (Eph. 1:4)."),
            2: ("*That there are various kinds of election of God unto eternal life: the one general and indefinite, "
                "the other particular and definite; and that the latter in turn is either incomplete, revocable, "
                "nondecisive and conditional, or complete, irrevocable, decisive and absolute. Likewise: that there "
                "is one election unto faith and another unto salvation, so that election can be unto justifying faith "
                "without being a decisive election unto salvation.*\n\n>For this is a fancy of men’s minds, "
                "invented regardless of the Scriptures, whereby the doctrine of election is corrupted, "
                "and this golden chain of our salvation is broken: \"Moreover whom He did predestinate, them He also "
                "called: and whom He called, them He also justified: and whom He justified, them He also glorified\" "
                "(Rom. 8:30)"),
            3: ("*That the good pleasure and purpose of God, of which Scripture makes mention in the doctrine of "
                "election, does not consist in this, that God chose certain persons rather than others, but in this, "
                "that He chose out of all possible conditions (among which are also the works of the law), "
                "or out of the whole order of things, the act of faith which from its very nature is undeserving, "
                "as well as its incomplete obedience, as a condition of salvation, and that He would graciously "
                "consider this in itself as a complete obedience and count it worthy of the reward of eternal "
                "life*\n\n>For by this injurious error the pleasure of God and the merits of Christ are made of none "
                "effect, and men are drawn away by useless questions from the truth of gracious justification and "
                "from the simplicity of Scripture, and this declaration of the apostle is charged as untrue: \"Who "
                "hath saved us, and called us with an holy calling, not according to our works, but according to His "
                "own purpose and grace, which was given us in Christ Jesus before the world began\" (2 Tim. 1:9)"),
            4: ("*That in the election unto faith this condition is beforehand demanded, namely, that man should use "
                "the light of nature aright, be pious, humble, meek, and fit for eternal life, as if on these things "
                "election were in any way dependent*\n\n>For this savors of the teaching of Pelagius, and is opposed "
                "to the doctrine of the apostle, when he writes: \"Among whom also we all had our conversation in "
                "times past in the lusts of our flesh, fulfilling the desires of the flesh and of the mind; and were "
                "by nature the children of wrath, even as others. But God, who is rich in mercy, for His great love "
                "wherewith He loved us, even when we were dead in sins, hath quickened us together with Christ, "
                "(by grace ye are saved;) and hath raised us up together, and made us sit together in heavenly places "
                "in Christ Jesus: that in the ages to come He might show the exceeding riches of His grace in His "
                "kindness toward us through Christ Jesus. For by grace are ye saved through faith; and that not of "
                "yourselves: it is the gift of God: not of works, lest any man should boast\" (Eph. 2:3–9)."),
            5: ("*That the incomplete and non-decisive election of particular persons to salvation occurred because "
                "of a foreseen faith, conversion, holiness, godliness, which either began or continued for some time; "
                "but that the complete and decisive election occurred because of foreseen perseverance unto the end "
                "in faith, conversion, holiness and godliness; and that this is the gracious and evangelical "
                "worthiness for the sake of which he who is chosen is more worthy than he who is not chosen; and that "
                "therefore faith, the obedience of faith, holiness, godliness and perseverance are not fruits of the "
                "unchangeable election unto glory, but are conditions, which, being required beforehand, "
                "were foreseen as being met by those who will be fully elected, and are causes without which the "
                "unchangeable election to glory does not occur.*\n\n>This is repugnant to the entire Scripture which "
                "constantly inculcates this and similar declarations: Election is not out of works, but of Him that "
                "calleth. \"That the purpose of God according to election might stand, not of works, but of Him that "
                "calleth\" (Rom. 9:11). \"And as many as were ordained to eternal life believed\" (Acts 13:48). \"He "
                "hath chosen us in Him before the foundation of the world, that we should be holy\" (Eph. 1:4). \"Ye "
                "have not chosen Me, but I have chosen you\" (John 15:16). \"But if it be of works, then is it no "
                "more grace\" (Rom. 11:6). \"Herein is love, not that we loved God, but that He loved us, "
                "and sent His Son\" (1 John 4:10)."),
            6: ("*That not every election unto salvation is unchangeable, but that some of the elect, any decree of "
                "God notwithstanding, can yet perish and do indeed perish.*\n\n>By which gross error they make God to "
                "be changeable, and destroy the comfort which the godly obtain out of the firmness of their election, "
                "and contradict the Holy Scripture which teaches that the elect cannot be led astray: \"Insomuch "
                "that, if it were possible, they shall deceive the very elect\" (Matt. 24:24); that Christ does not "
                "lose those whom the Father gave Him: \"And this is the Father's will which hath sent Me, that of all "
                "which He hath given Me I should lose nothing\" (John 6:39); and that God hath also glorified those "
                "whom He foreordained, called and justified: \"Moreover whom He did predestinate, them He also "
                "called: and whom He called, them He also justified: and whom He justified, them He also glorified\" "
                "(Rom. 8:30)."),
            7: ("*That there is in this life no fruit and no consciousness of the unchangeable election to glory, "
                "nor any certainty, except that which depends on a changeable and uncertain condition.*\n\n>For not "
                "only is it absurd to speak of an uncertain certainty, but also contrary to the experience of the "
                "saints, who by virtue of the consciousness of their election rejoice with the apostle and praise "
                "this favor of God, Ephesians 1; who according to Christ's admonition rejoice with His disciples that "
                "their names are written in heaven, \"but rather rejoice, because your names are written in heaven\" "
                "(Luke 10:20); who also place the consciousness of their election over against the fiery darts of the "
                "devil, asking: \"Who shall lay any thing to the charge of God's elect?\" (Rom. 8:33)."),
            8: ("*That God, simply by virtue of His righteous will, did not decide either to leave anyone in the fall "
                "of Adam and in the common state of sin and condemnation, or to pass anyone by in the communication "
                "of grace which is necessary for faith and conversion.*\n\n>For this is firmly decreed: \"Therefore "
                "hath He mercy on whom He will have mercy, and whom He will He hardeneth\" (Rom. 9:18). And also "
                "this: \"It is given unto you to know the mysteries of the kingdom of heaven, but to them it is not "
                "given\" (Matt. 13:11). Likewise: \"I thank Thee, O Father, Lord of heaven and earth, because Thou "
                "hast hid these things from the wise and prudent, and hast revealed them unto babes. Even so, "
                "Father: for so it seemed good in Thy sight\" (Matt. 11:25–26)"),
            9: ("*That the reason why God sends the gospel to one people rather than to another is not merely and "
                "solely the good pleasure of God, but rather the fact that one people is better and worthier than "
                "another to whom the gospel is not communicated.*\n\n>For this Moses denies, addressing the people of "
                "Israel as follows: \"Behold, the heaven and the heaven of heavens is the LORD'S thy God, "
                "the earth also, with all that therein is. Only the LORD had a delight in thy fathers to love them, "
                "and He chose their seed after them, even you above all people, as it is this day\" (Deut. 10:14–15). "
                "And Christ said: \"Woe unto thee, Chorazin! woe unto thee, Bethsaida! for if the mighty works, "
                "which were done in you, had been done in Tyre and Sidon, they would have repented long ago in "
                "sackcloth and ashes\" (Matt. 11:21).")
        },
        2: {
            0: "**SECOND HEAD OF DOCTRINE**\n\n>**Of the Death of Christ and the Redemption of Men Thereby**",
            1: ("*That God the Father has ordained His Son to the death of the cross without a certain and definite "
                "decree to save any, so that the necessity, profitableness and worth of what Christ merited by His "
                "death might have existed, and might remain in all its parts complete, perfect and intact, "
                "even if the merited redemption had never in fact been applied to any person.*\n\n>For this doctrine "
                "tends to the despising of the wisdom of the Father and of the merits of Jesus Christ, "
                "and is contrary to Scripture. For thus saith our Savior: \"I lay down My life for the sheep, "
                "and I know them\" (John 10:15, 27). And the prophet Isaiah saith concerning the Savior: \"When thou "
                "shalt make His soul an offering for sin, He shall see His seed, He shall prolong his days, "
                "and the pleasure of the LORD shall prosper in his hand\" (Is. 53:10). Finally, this contradicts the "
                "article of faith according to which we believe the catholic Christian church."),
            2: ("*That it was not the purpose of the death of Christ that He should confirm the new covenant of grace "
                "through His blood, but only that He should acquire for the Father the mere right to establish with "
                "man such a covenant as He might please, whether of grace or of works.*\n\n>For this is repugnant to "
                "Scripture which teaches that Christ has become the Surety and Mediator of a better, that is, "
                "the new covenant, and that a testament is of force where death has occurred. \"By so much was Jesus "
                "made a surety of a better testament\" (Heb. 7:22); \"And for this cause He is the Mediator of the "
                "new testament, that by means of death, for the redemption of the transgressions that were under the "
                "first testament, they which are called might receive the promise of eternal inheritance\"; \"For a "
                "testament is of force after men are dead: otherwise it is of no strength at all while the testator "
                "liveth\" (Heb. 9:15, 17)."),
            3: ("*That Christ by His satisfaction merited neither salvation itself for anyone, nor faith, "
                "whereby this satisfaction of Christ unto salvation is effectually appropriated; but that He merited "
                "for the Father only the authority or the perfect will to deal again with man, and to prescribe new "
                "conditions as He might desire, obedience to which, however, depended on the free will of man, "
                "so that it therefore might have come to pass that either none or all should fulfill these "
                "conditions.*\n\n>For these adjudge too contemptuously of the death of Christ, do in no wise "
                "acknowledge the most important fruit or benefit thereby gained, and bring again out of hell the "
                "Pelagian error."),
            4: ("*That the new covenant of grace, which God the Father, through the mediation of the death of Christ, "
                "made with man, does not herein consist that we by faith, inasmuch as it accepts the merits of "
                "Christ, are justified before God and saved, but in the fact that God having revoked the demand of "
                "perfect obedience of faith, regards faith itself and the obedience of faith, although imperfect, "
                "as the perfect obedience of the law, and does esteem it worthy of the reward of eternal life through "
                "grace.*\n\n>For these contradict the Scriptures: \"Being justified freely by His grace through the "
                "redemption that is in Christ Jesus: whom God hath set forth to be a propitiation through faith in "
                "His blood\" (Rom. 3:24–25). And these proclaim, as did the wicked Socinus, a new and strange "
                "justification of man before God against the consensus of the whole church."),
            5: ("*That all men have been accepted unto the state of reconciliation and unto the grace of the "
                "covenant, so that no one is worthy of condemnation on account of original sin, and that no one shall "
                "be condemned because of it, but that all are free from the guilt of original sin*\n\n>For this "
                "opinion is repugnant to Scripture which teaches that we are by nature children of wrath (Eph. 2:3)."),
            6: ("*The use of the difference between meriting and appropriating, to the end that they may instill into "
                "the minds of the imprudent and inexperienced this teaching that God, as far as He is concerned, "
                "has been minded of applying to all equally the benefits gained by the death of Christ; but that, "
                "while some obtain the pardon of sin and eternal life, and others do not, this difference depends on "
                "their own free will, which joins itself to the grace that is offered without exception, and that it "
                "is not dependent on the special gift of mercy, which powerfully works in them, that they rather than "
                "others should appropriate unto themselves this grace.*\n\n>For these, while they feign that they "
                "present this distinction in a sound sense, seek to instill into the people the destructive poison of "
                "the Pelagian errors"),
            7: ("*That Christ neither could die, needed to die, nor did die for those whom God loved in the highest "
                "degree and elected to eternal life, and did not die for these, since these do not need the death of "
                "Christ.*\n\n>For they contradict the apostle, who declares: \"the Son of God, who loved me, "
                "and gave Himself for me\" (Gal. 2:20). Likewise: \"Who shall lay any thing to the charge of God's "
                "elect? It is God that justifieth. Who is he that condemneth? It is Christ that died\" (Rom. "
                "8:33–34), namely, for them; and the Savior who says: \"I lay down My life for the sheep\" (John "
                "10:15). And: \"This is My commandment, That ye love one another, as I have loved you. Greater love "
                "hath no man than this, that a man lay down his life for his friends\" (John 15:12–13).")
        },
        3: {
            0: ("**THIRD AND FOURTH HEADS OF DOCTRINE**\n\n>**Of the Corruption of Man, His Conversion to God, "
                "and the Manner Thereof**"),
            1: ("*That it cannot properly be said that original sin in itself suffices to condemn the whole human "
                "race or to deserve temporal and eternal punishment.*\n\n>For these contradict the apostle, "
                "who declares: \"Wherefore, as by one man sin entered into the world, and death by sin; and so death "
                "passed upon all men, for that all have sinned\" (Rom. 5:12). And: \"The judgment was by one to "
                "condemnation\" (Rom. 5:16). And: \"The wages of sin is death\" (Rom. 6:23)."),
            2: ("*That the spiritual gifts or the good qualities and virtues, such as goodness, holiness, "
                "righteousness, could not belong to the will of man when he was first created, and that these, "
                "therefore, could not have been separated therefrom in the fall.*\n\n>For such is contrary to the "
                "description of the image of God which the apostle gives in Ephesians 4:24, where he declares that it "
                "consists in righteousness and holiness, which undoubtedly belong to the will."),
            3: ("*That in spiritual death the spiritual gifts are not separate from the will of man, since the will "
                "in itself has never been corrupted, but only hindered through the darkness of the understanding and "
                "the irregularity of the affections; and that, these hindrances having been removed, the will can "
                "then bring into operation its native powers, that is, that the will of itself is able to will and to "
                "choose, or not to will and not to choose, all manner of good which may be presented to it.*\n\n>This "
                "is an innovation and an error, and tends to elevate the powers of the free will, contrary to the "
                "declaration of the prophet: \"The heart is deceitful above all things, and desperately wicked\" ("
                "Jer. 17:9); and of the apostle: \"Among whom (sons of disobedience) also we all had our conversation "
                "in times past in the lusts of our flesh, fulfilling the desires of the flesh and of the mind\" (Eph. "
                "2:3)."),
            4: ("*That the unregenerate man is not really nor utterly dead in sin, nor destitute of all powers unto "
                "spiritual good, but that he can yet hunger and thirst after righteousness and life, and offer the "
                "sacrifice of a contrite and broken spirit, which is pleasing to God*\n\n>For these are contrary to "
                "the express testimony of Scripture. \"Who were dead in trespasses and sins\"; \"Even when we were "
                "dead in sins\" (Eph. 2:1, 5); and: \"every imagination of the thoughts of his heart was only evil "
                "continually\" (Gen. 6:5); \"for the imagination of man's heart is evil from his youth\" (Gen. "
                "8:21).\n\n>Moreover, to hunger and thirst after deliverance from misery, and after life, "
                "and to offer unto God the sacrifice of a broken spirit, is peculiar to the regenerate and those that "
                "are called blessed. \"Create in me a clean heart, O God; and renew a right spirit within me\"; "
                "\"Then shalt Thou be pleased with the sacrifices of righteousness, with burnt offering and whole "
                "burnt offering: then shall they offer bullocks upon Thine altar\" (Ps. 51:10, 19); \"Blessed are "
                "they which do hunger and thirst after righteousness: for they shall be filled\" (Matt. 5:6)."),
            5: ("*That the corrupt and natural man can so well use the common grace (by which they understand the "
                "light of nature), or the gifts still left him after the fall, that he can gradually gain by their "
                "good use a greater, namely, the evangelical or saving grace and salvation itself. And that in this "
                "way God on His part shows Himself ready to reveal Christ unto all men, since He applies to all "
                "sufficiently and efficiently the means necessary to conversion.*\n\n>For the experience of all ages "
                "and the Scriptures do both testify that this is untrue. \"He sheweth His word unto Jacob, "
                "His statutes and His judgments unto Israel. He hath not dealt so with any nation: and as for His "
                "judgments, they have not known them\" (Ps. 147:19, 20). \"Who in times past suffered all nations to "
                "walk in their own ways\" (Acts 14:16). And: \"Now when they (Paul and his companions) had gone "
                "throughout Phrygia and the region of Page 13 Galatia, and were forbidden of the Holy Ghost to preach "
                "the word in Asia, after they were come to Mysia, they assayed to go into Bithynia: but the Spirit "
                "suffered them not\" (Acts 16:6, 7)."),
            6: ("*That in the true conversion of man no new qualities, powers or gifts can be infused by God into the "
                "will, and that therefore faith through which we are first converted, and because of which we are "
                "called believers, is not a quality or gift infused by God, but only an act of man, and that it "
                "cannot be said to be a gift, except in respect of the power to attain to this faith.*\n\n>For "
                "thereby they contradict the Holy Scriptures which declare that God infuses new qualities of faith, "
                "of obedience, and of the consciousness of His love into our hearts: \"I will put My law in their "
                "inward parts, and write it in their hearts\" (Jer. 31:33). And: \"I will pour water upon him that is "
                "thirsty, and floods upon the dry ground: I will pour My Spirit upon thy seed\" (Is. 44:3). And: "
                "\"the love of God is shed abroad in our hearts by the Holy Ghost which is given unto us\" (Rom. "
                "5:5). This is also repugnant to the continuous practice of the Church, which prays by the mouth of "
                "the prophet thus: \"turn Thou me, and I shall be turned\" (Jer. 31:18)."),
            7: ("*That the grace whereby we are converted to God is only a gentle advising, or (as others explain "
                "it), that this is the noblest manner of working in the conversion of man, and that this manner of "
                "working, which consists in advising, is most in harmony with man's nature; and that there is no "
                "reason why this advising grace alone should not be sufficient to make the natural man spiritual, "
                "indeed, that God does not produce the consent of the will except through this manner of advising; "
                "and that the power of the divine working, whereby it surpasses the working of Satan, consists in "
                "this, that God promises eternal, while Satan promises only temporal goods.*\n\n>But this is "
                "altogether Pelagian and contrary to the whole Scripture which, besides this, teaches yet another and "
                "far more powerful and divine manner of the Holy Spirit's working in the conversion of man, "
                "as in Ezekiel: \"A new heart also will I give you, and a new spirit will I put within you: and I "
                "will take away the stony heart out of your flesh, and I will give you an heart of flesh\" (Ezek. "
                "36:26)."),
            8: ("*That God in the regeneration of man does not use such powers of His omnipotence as potently and "
                "infallibly bend man's will to faith and conversion; but that all the works of grace having been "
                "accomplished, which God employs to convert man, man may yet so resist God and the Holy Spirit when "
                "God intends man's regeneration and wills to regenerate him, and indeed that man often does so resist "
                "that he prevents entirely his regeneration, and that it therefore remains in man's power to be "
                "regenerated or not*\n\n>For this is nothing less than the denial of all the efficiency of God's "
                "grace in our conversion, and the subjecting of the working of the Almighty God to the will of man, "
                "which is contrary to the apostles, who teach: \"who believe, according to the working of His mighty "
                "power\" (Eph. 1:19). And: \"That our God would...fulfil all the good pleasure of His goodness, "
                "and the work of faith with power\" (2 Thess. 1:11). And: \"According as His divine power hath given "
                "unto us all things that pertain unto life and godliness\" (2 Pet. 1:3)."),
            9: ("*That grace and free will are partial causes, which together work the beginning of conversion, "
                "and that grace, in order of working, does not precede the working of the will; that is, "
                "that God does not efficiently help the will of man unto conversion until the will of man moves and "
                "determines to do this.*\n\n>For the ancient Church has long ago condemned this doctrine of the "
                "Pelagians according to the words of the apostle: \"So then it is not of him that willeth, "
                "nor of him that runneth, but of God that sheweth mercy\" (Rom. 9:16). Likewise: \"For who maketh "
                "thee to differ from another? and what hast thou that thou didst not receive?\" (1 Cor. 4:7). And: "
                "\"For it is God which worketh in you both to will and to do of His good pleasure\" (Phil. 2:13).")
        },
        4: {
            0: ("**THIRD AND FOURTH HEADS OF DOCTRINE**\n\n>**Of the Corruption of Man, His Conversion to God, "
                "and the Manner Thereof**"),
            1: ("*That it cannot properly be said that original sin in itself suffices to condemn the whole human "
                "race or to deserve temporal and eternal punishment.*\n\n>For these contradict the apostle, "
                "who declares: \"Wherefore, as by one man sin entered into the world, and death by sin; and so death "
                "passed upon all men, for that all have sinned\" (Rom. 5:12). And: \"The judgment was by one to "
                "condemnation\" (Rom. 5:16). And: \"The wages of sin is death\" (Rom. 6:23)."),
            2: ("*That the spiritual gifts or the good qualities and virtues, such as goodness, holiness, "
                "righteousness, could not belong to the will of man when he was first created, and that these, "
                "therefore, could not have been separated therefrom in the fall.*\n\n>For such is contrary to the "
                "description of the image of God which the apostle gives in Ephesians 4:24, where he declares that it "
                "consists in righteousness and holiness, which undoubtedly belong to the will."),
            3: ("*That in spiritual death the spiritual gifts are not separate from the will of man, since the will "
                "in itself has never been corrupted, but only hindered through the darkness of the understanding and "
                "the irregularity of the affections; and that, these hindrances having been removed, the will can "
                "then bring into operation its native powers, that is, that the will of itself is able to will and to "
                "choose, or not to will and not to choose, all manner of good which may be presented to it.*\n\n>This "
                "is an innovation and an error, and tends to elevate the powers of the free will, contrary to the "
                "declaration of the prophet: \"The heart is deceitful above all things, and desperately wicked\" ("
                "Jer. 17:9); and of the apostle: \"Among whom (sons of disobedience) also we all had our conversation "
                "in times past in the lusts of our flesh, fulfilling the desires of the flesh and of the mind\" (Eph. "
                "2:3)."),
            4: ("*That the unregenerate man is not really nor utterly dead in sin, nor destitute of all powers unto "
                "spiritual good, but that he can yet hunger and thirst after righteousness and life, and offer the "
                "sacrifice of a contrite and broken spirit, which is pleasing to God*\n\n>For these are contrary to "
                "the express testimony of Scripture. \"Who were dead in trespasses and sins\"; \"Even when we were "
                "dead in sins\" (Eph. 2:1, 5); and: \"every imagination of the thoughts of his heart was only evil "
                "continually\" (Gen. 6:5); \"for the imagination of man's heart is evil from his youth\" (Gen. "
                "8:21).\n\n>Moreover, to hunger and thirst after deliverance from misery, and after life, "
                "and to offer unto God the sacrifice of a broken spirit, is peculiar to the regenerate and those that "
                "are called blessed. \"Create in me a clean heart, O God; and renew a right spirit within me\"; "
                "\"Then shalt Thou be pleased with the sacrifices of righteousness, with burnt offering and whole "
                "burnt offering: then shall they offer bullocks upon Thine altar\" (Ps. 51:10, 19); \"Blessed are "
                "they which do hunger and thirst after righteousness: for they shall be filled\" (Matt. 5:6)."),
            5: ("*That the corrupt and natural man can so well use the common grace (by which they understand the "
                "light of nature), or the gifts still left him after the fall, that he can gradually gain by their "
                "good use a greater, namely, the evangelical or saving grace and salvation itself. And that in this "
                "way God on His part shows Himself ready to reveal Christ unto all men, since He applies to all "
                "sufficiently and efficiently the means necessary to conversion.*\n\n>For the experience of all ages "
                "and the Scriptures do both testify that this is untrue. \"He sheweth His word unto Jacob, "
                "His statutes and His judgments unto Israel. He hath not dealt so with any nation: and as for His "
                "judgments, they have not known them\" (Ps. 147:19, 20). \"Who in times past suffered all nations to "
                "walk in their own ways\" (Acts 14:16). And: \"Now when they (Paul and his companions) had gone "
                "throughout Phrygia and the region of Page 13 Galatia, and were forbidden of the Holy Ghost to preach "
                "the word in Asia, after they were come to Mysia, they assayed to go into Bithynia: but the Spirit "
                "suffered them not\" (Acts 16:6, 7)."),
            6: ("*That in the true conversion of man no new qualities, powers or gifts can be infused by God into the "
                "will, and that therefore faith through which we are first converted, and because of which we are "
                "called believers, is not a quality or gift infused by God, but only an act of man, and that it "
                "cannot be said to be a gift, except in respect of the power to attain to this faith.*\n\n>For "
                "thereby they contradict the Holy Scriptures which declare that God infuses new qualities of faith, "
                "of obedience, and of the consciousness of His love into our hearts: \"I will put My law in their "
                "inward parts, and write it in their hearts\" (Jer. 31:33). And: \"I will pour water upon him that is "
                "thirsty, and floods upon the dry ground: I will pour My Spirit upon thy seed\" (Is. 44:3). And: "
                "\"the love of God is shed abroad in our hearts by the Holy Ghost which is given unto us\" (Rom. "
                "5:5). This is also repugnant to the continuous practice of the Church, which prays by the mouth of "
                "the prophet thus: \"turn Thou me, and I shall be turned\" (Jer. 31:18)."),
            7: ("*That the grace whereby we are converted to God is only a gentle advising, or (as others explain "
                "it), that this is the noblest manner of working in the conversion of man, and that this manner of "
                "working, which consists in advising, is most in harmony with man's nature; and that there is no "
                "reason why this advising grace alone should not be sufficient to make the natural man spiritual, "
                "indeed, that God does not produce the consent of the will except through this manner of advising; "
                "and that the power of the divine working, whereby it surpasses the working of Satan, consists in "
                "this, that God promises eternal, while Satan promises only temporal goods.*\n\n>But this is "
                "altogether Pelagian and contrary to the whole Scripture which, besides this, teaches yet another and "
                "far more powerful and divine manner of the Holy Spirit's working in the conversion of man, "
                "as in Ezekiel: \"A new heart also will I give you, and a new spirit will I put within you: and I "
                "will take away the stony heart out of your flesh, and I will give you an heart of flesh\" (Ezek. "
                "36:26)."),
            8: ("*That God in the regeneration of man does not use such powers of His omnipotence as potently and "
                "infallibly bend man's will to faith and conversion; but that all the works of grace having been "
                "accomplished, which God employs to convert man, man may yet so resist God and the Holy Spirit when "
                "God intends man's regeneration and wills to regenerate him, and indeed that man often does so resist "
                "that he prevents entirely his regeneration, and that it therefore remains in man's power to be "
                "regenerated or not*\n\n>For this is nothing less than the denial of all the efficiency of God's "
                "grace in our conversion, and the subjecting of the working of the Almighty God to the will of man, "
                "which is contrary to the apostles, who teach: \"who believe, according to the working of His mighty "
                "power\" (Eph. 1:19). And: \"That our God would...fulfil all the good pleasure of His goodness, "
                "and the work of faith with power\" (2 Thess. 1:11). And: \"According as His divine power hath given "
                "unto us all things that pertain unto life and godliness\" (2 Pet. 1:3)."),
            9: ("*That grace and free will are partial causes, which together work the beginning of conversion, "
                "and that grace, in order of working, does not precede the working of the will; that is, "
                "that God does not efficiently help the will of man unto conversion until the will of man moves and "
                "determines to do this.*\n\n>For the ancient Church has long ago condemned this doctrine of the "
                "Pelagians according to the words of the apostle: \"So then it is not of him that willeth, "
                "nor of him that runneth, but of God that sheweth mercy\" (Rom. 9:16). Likewise: \"For who maketh "
                "thee to differ from another? and what hast thou that thou didst not receive?\" (1 Cor. 4:7). And: "
                "\"For it is God which worketh in you both to will and to do of His good pleasure\" (Phil. 2:13).")
        }
    }

    __cdrRegex = r"\[\s*(?:C|Canons)\s*(?:of)?\s*(?:D|Dort|Dordt)\s*(?:R|Rejection|Rejections)\s*([\d\,\-\:\s.]+)\]"

    def __init__(self):
        self.__parse = chapter_paragraph_parser

    def __get_text(self, from_chptr, from_para, to_chptr, to_para):
        if (0 < from_chptr <= to_chptr <= 4) and \
                (0 < from_para <= self.__CHPTRMAX[from_chptr]) and \
                (0 < to_para <= self.__CHPTRMAX[to_chptr]):
            result = ''
            for i in range(from_chptr, to_chptr + 1):
                result += "\n>" + self.__text[i][0] + "\n\n"
                for j in range(from_para if i == from_chptr else 1,
                               to_para + 1 if i == to_chptr else self.__CHPTRMAX[i] + 1):
                    result += ">**Rejection " + str(j) + "**\n\n>" + self.__text[i][j] + "\n\n"
            return result, False
        else:
            return '', True

    def fetch(self, full_citations):
        response_text = ''
        response_citation = ''
        response_is_malformed = False

        if full_citations:
            cdr_citations = re.findall(self.__cdrRegex, full_citations, re.IGNORECASE)
            if cdr_citations:
                response_citation = '[CDR '
                args, response_is_malformed = self.__parse(cdr_citations)
                for i in args:
                    response_citation += str(i[0]) + ':' + str(i[1]) + "-" + str(i[2]) + ':' + str(i[3]) + ", "
                    quote, temp = self.__get_text(i[0], i[1], i[2], i[3])
                    response_is_malformed |= temp
                    if response_text:
                        response_text += quote
                    elif quote:
                        response_text += "\n**Canons of Dort**\n" + quote
                response_citation = response_citation[:-2] + "]"
        return response_text, response_citation, response_is_malformed