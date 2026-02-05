// MBTI Personality Types Data
// All 16 personality types with descriptions and characteristics

export interface PersonalityType {
    code: string;
    name: string;
    nickname: string;
    description: string;
    traits: string[];
    strengths: string[];
    color: string;
}

export const personalityTypes: Record<string, PersonalityType> = {
    INTJ: {
        code: "INTJ",
        name: "Architect",
        nickname: "The Mastermind",
        description: "Imaginative and strategic thinkers with a plan for everything. INTJs are analytical problem-solvers, eager to improve systems and processes with their innovative ideas.",
        traits: ["Strategic", "Independent", "Determined", "Innovative"],
        strengths: ["High standards", "Quick learners", "Self-confident", "Hard-working"],
        color: "#6B5B95",
    },
    INTP: {
        code: "INTP",
        name: "Logician",
        nickname: "The Thinker",
        description: "Innovative inventors with an unquenchable thirst for knowledge. INTPs are logical and objective, enjoying theoretical and abstract concepts.",
        traits: ["Analytical", "Original", "Open-minded", "Curious"],
        strengths: ["Great analysts", "Abstract thinking", "Imaginative", "Objective"],
        color: "#88B04B",
    },
    ENTJ: {
        code: "ENTJ",
        name: "Commander",
        nickname: "The Leader",
        description: "Bold, imaginative and strong-willed leaders, always finding a way or making one. ENTJs are decisive and love momentum and accomplishment.",
        traits: ["Efficient", "Energetic", "Strategic", "Charismatic"],
        strengths: ["Natural leaders", "Efficient", "Self-confident", "Strong-willed"],
        color: "#F7CAC9",
    },
    ENTP: {
        code: "ENTP",
        name: "Debater",
        nickname: "The Visionary",
        description: "Smart and curious thinkers who cannot resist an intellectual challenge. ENTPs are energetic and love to argue for the sake of intellectual challenge.",
        traits: ["Quick", "Ingenious", "Outspoken", "Resourceful"],
        strengths: ["Knowledgeable", "Quick thinkers", "Charismatic", "Energetic"],
        color: "#92A8D1",
    },
    INFJ: {
        code: "INFJ",
        name: "Advocate",
        nickname: "The Counselor",
        description: "Quiet and mystical, yet very inspiring and tireless idealists. INFJs are deep thinkers with a strong sense of purpose and meaning.",
        traits: ["Insightful", "Principled", "Compassionate", "Idealistic"],
        strengths: ["Creative", "Decisive", "Passionate", "Altruistic"],
        color: "#955251",
    },
    INFP: {
        code: "INFP",
        name: "Mediator",
        nickname: "The Healer",
        description: "Poetic, kind and altruistic people, always eager to help a good cause. INFPs are idealistic and empathetic, guided by their core values.",
        traits: ["Empathetic", "Creative", "Idealistic", "Open-minded"],
        strengths: ["Passionate", "Generous", "Creative", "Dedicated"],
        color: "#B565A7",
    },
    ENFJ: {
        code: "ENFJ",
        name: "Protagonist",
        nickname: "The Teacher",
        description: "Charismatic and inspiring leaders, able to mesmerize their listeners. ENFJs are natural-born leaders with a passion for helping others reach their potential.",
        traits: ["Warm", "Empathetic", "Charismatic", "Organized"],
        strengths: ["Tolerant", "Reliable", "Natural leaders", "Altruistic"],
        color: "#009B77",
    },
    ENFP: {
        code: "ENFP",
        name: "Campaigner",
        nickname: "The Champion",
        description: "Enthusiastic, creative and sociable free spirits, who can always find a reason to smile. ENFPs are passionate about new ideas and possibilities.",
        traits: ["Enthusiastic", "Creative", "Sociable", "Optimistic"],
        strengths: ["Curious", "Observant", "Energetic", "Popular"],
        color: "#DD4124",
    },
    ISTJ: {
        code: "ISTJ",
        name: "Logistician",
        nickname: "The Inspector",
        description: "Practical and fact-minded individuals, whose reliability cannot be doubted. ISTJs are responsible and dependable, committed to traditions and standards.",
        traits: ["Responsible", "Thorough", "Dependable", "Calm"],
        strengths: ["Honest", "Direct", "Strong-willed", "Patient"],
        color: "#45B8AC",
    },
    ISFJ: {
        code: "ISFJ",
        name: "Defender",
        nickname: "The Protector",
        description: "Very dedicated and warm protectors, always ready to defend their loved ones. ISFJs are supportive and loyal, with a strong sense of duty.",
        traits: ["Supportive", "Reliable", "Patient", "Observant"],
        strengths: ["Loyal", "Hard-working", "Imaginative", "Practical"],
        color: "#EFC050",
    },
    ESTJ: {
        code: "ESTJ",
        name: "Executive",
        nickname: "The Supervisor",
        description: "Excellent administrators, unsurpassed at managing things and people. ESTJs are organized and dedicated to upholding traditions and rules.",
        traits: ["Organized", "Logical", "Assertive", "Focused"],
        strengths: ["Dedicated", "Strong-willed", "Direct", "Loyal"],
        color: "#5B5EA6",
    },
    ESFJ: {
        code: "ESFJ",
        name: "Consul",
        nickname: "The Provider",
        description: "Extraordinarily caring, social and popular people, always eager to help. ESFJs are warm-hearted and conscientious, committed to their duties.",
        traits: ["Caring", "Sociable", "Loyal", "Sensitive"],
        strengths: ["Strong practical skills", "Loyal", "Warm", "Connecting with others"],
        color: "#9B2335",
    },
    ISTP: {
        code: "ISTP",
        name: "Virtuoso",
        nickname: "The Craftsman",
        description: "Bold and practical experimenters, masters of all kinds of tools. ISTPs are optimistic and energetic with a keen eye for detail.",
        traits: ["Practical", "Observant", "Analytical", "Reserved"],
        strengths: ["Optimistic", "Creative", "Practical", "Spontaneous"],
        color: "#DFCFBE",
    },
    ISFP: {
        code: "ISFP",
        name: "Adventurer",
        nickname: "The Composer",
        description: "Flexible and charming artists, always ready to explore and experience something new. ISFPs are gentle souls with a strong aesthetic sense.",
        traits: ["Artistic", "Sensitive", "Caring", "Peaceful"],
        strengths: ["Charming", "Imaginative", "Passionate", "Curious"],
        color: "#E15D44",
    },
    ESTP: {
        code: "ESTP",
        name: "Entrepreneur",
        nickname: "The Dynamo",
        description: "Smart, energetic and very perceptive people, who truly enjoy living on the edge. ESTPs are action-oriented and resourceful.",
        traits: ["Energetic", "Perceptive", "Bold", "Direct"],
        strengths: ["Bold", "Rational", "Practical", "Original"],
        color: "#7FCDCD",
    },
    ESFP: {
        code: "ESFP",
        name: "Entertainer",
        nickname: "The Performer",
        description: "Spontaneous, energetic and enthusiastic entertainers – life is never boring around them. ESFPs are vivacious and enjoy the spotlight.",
        traits: ["Spontaneous", "Energetic", "Friendly", "Playful"],
        strengths: ["Bold", "Original", "Practical", "Observant"],
        color: "#BC243C",
    },
};

// Get personality type by code
export const getPersonalityType = (code: string): PersonalityType | undefined => {
    return personalityTypes[code.toUpperCase()];
};

// All personality types as array
export const allPersonalityTypes = Object.values(personalityTypes);
