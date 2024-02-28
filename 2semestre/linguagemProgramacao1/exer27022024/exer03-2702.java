import java.util.Scanner;

public class CalcularNotaLP {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Entrada de dados
        System.out.println("Informe a nota da P1:");
        double P1 = scanner.nextDouble();
        System.out.println("Informe a nota da E1:");
        double E1 = scanner.nextDouble();
        System.out.println("Informe a nota da E2:");
        double E2 = scanner.nextDouble();
        System.out.println("Informe a nota da API:");
        double API = scanner.nextDouble();
        System.out.println("Informe a nota do X:");
        double X = scanner.nextDouble();
        System.out.println("Informe a nota do SUB:");
        double SUB = scanner.nextDouble();

        // Calcular a nota dos alunos (1° tentativa)
        /*double nota = (P1 * 0.6 + ((E1 + E2) / 2) * 0.4) * 0.5 +
                      (Math.max(((P1 * 0.6 + ((E1 + E2) / 2) * 0.4) - 5.9), 0) /
                      ((P1 * 0.6 + ((E1 + E2) / 2) * 0.4) - 5.9)) * (API * 0.5) + X + (SUB * 0.2);*/



        // Exemplo para tentiva de condicional

        if (estoque >= 100) {
	           System.out.println(“Produto com quantidade suficiente.”);
        } else if (estoque < 100 && estoque > 50) {
	        System.out.println(“Alerta: Avaliar possibilidade de novo pedido.”);
        } else {
	        System.out.println(“ATENÇÃO! Faça um novo pedido.”);
        }

        
        

      // Usar a fórumla da LP pra grar o calculo

        // Exibindo a nota calculada
        System.out.println("A nota final do aluno é: " + nota);

        scanner.close();
    }
}
