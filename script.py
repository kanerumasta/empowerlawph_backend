from datetime import date
from random import randint
from case.models import Case

def create_case(title, number, decision_date, ponente, division, full_text):
    case = Case(
        title=title,
        number=number,
        decision_date=decision_date,
        ponente=ponente,
        division=division,
        full_text=full_text
    )
    case.save()

def generate_random_case_data():
    # Example random generation for the cases
    titles = [
        "Republic v. Juan Dela Cruz", "People v. Maria Clara", "Gonzales v. Pilipinas Corporation",
        "Sandiganbayan v. Garcia", "Republic of the Philippines v. Ernesto Reyes"
    ]
    divisions = ["First Division", "Second Division", "Third Division"]
    ponentes = ["Justice Santos", "Justice Reyes", "Justice Cruz", "Justice Hernandez", "Justice Mendoza"]
    case_numbers = [f"Criminal Case No. {randint(1000, 9999)}", f"Civil Case No. {randint(1000, 9999)}"]
    
    # Generate some sample long case texts
    full_texts = [
        "This case revolves around a detailed legal dispute where the accused, Juan Dela Cruz, was charged with multiple counts of fraud, embezzlement, and misrepresentation in connection with a large-scale corporate scam. The prosecution presented numerous witnesses who testified about the fraudulent activities in which the defendant was involved. The defense, on the other hand, argued that the evidence presented by the prosecution was circumstantial and lacked the necessary clarity to convict the defendant beyond a reasonable doubt. After reviewing the testimonies and the evidence provided, the Court concluded that the accused was guilty of the charges and imposed a severe penalty. This ruling is considered a landmark decision in corporate fraud cases in the Philippines.",
        
        "In this case, Maria Clara was accused of illegally appropriating funds from a public office, committing acts of dishonesty, and falsifying documents. The Court heard testimonies from government officials who confirmed the misconduct. The defense claimed that Maria Clara was a victim of a political conspiracy and that the charges were fabricated. After extensive deliberation, the Court found that the accused had indeed violated the law and sentenced her to a lengthy prison term. The judgment also outlined the Court's firm stance against corruption in public offices, setting a precedent for similar cases in the future.",
        
        "This case involves a civil dispute between Gonzales and the Philippines Corporation over a breach of contract related to an extensive construction project. The plaintiffs, Gonzales, accused the Corporation of failing to meet contractual obligations, resulting in severe financial losses. The Corporation denied the allegations, claiming that delays were caused by external factors, including unforeseen natural disasters. The Court analyzed the contract terms and the circumstances surrounding the dispute, ultimately ruling in favor of Gonzales, awarding them substantial damages for the Corporation's failure to fulfill the agreed-upon terms.",
        
        "The Sandiganbayan, in this case, found the accused, Garcia, guilty of corruption, illegal enrichment, and abuse of authority while holding a prominent position in government. Evidence was presented showing Garcia's lavish lifestyle, which could not be justified by his known income. The Court's decision reinforced the anti-corruption laws in the Philippines, sending a strong message that public officials will be held accountable for their illegal actions. The decision also outlined the importance of transparency and the need for strict enforcement of anti-corruption regulations in government offices.",
        
        "Ernesto Reyes was accused of conspiracy to commit murder in connection with a series of violent acts that resulted in the death of several individuals. The case involved several co-defendants, and the prosecution argued that Reyes was a key figure in the planning and execution of the murders. The defense, however, contended that Reyes was an innocent bystander and had no involvement in the killings. After considering the evidence, including testimonies from key witnesses and forensic reports, the Court found Reyes guilty and sentenced him to life imprisonment. This decision was hailed as an important ruling in the fight against organized crime and violence."
    ]
    
    decision_dates = [date(randint(2000, 2025), randint(1, 12), randint(1, 28)) for _ in range(30)]
    
    # Create 30 cases with random data
    for i in range(30):
        title = titles[randint(0, len(titles)-1)]
        number = case_numbers[randint(0, len(case_numbers)-1)]
        decision_date = decision_dates[i]
        ponente = ponentes[randint(0, len(ponentes)-1)]
        division = divisions[randint(0, len(divisions)-1)]
        full_text = full_texts[randint(0, len(full_texts)-1)]
        
        create_case(title, number, decision_date, ponente, division, full_text)

# Call the function to create the 30 cases
generate_random_case_data()
