public class CalculadoraDespesasTrimestre {
    public static void main(String[] args) {
        int janeiro = 15000;
        int fevereiro = 23000;
        int marco = 17000;

        int total = janeiro + fevereiro + marco;
        
        double media = total / 3.0;

        // Imprimindo os resultados
        System.out.println("Despesa total no trimestre: R$" + total);
        System.out.println("Média mensal de gastos: R$" + media);
    }
}
