import java.util.Scanner;

/* HelloWorld.java
 */

public class c
{

    
	public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
		System.out.println("Hello World!");
        int a = s.nextInt();
        int b = 100;
        System.out.println(a + b);
	}

    public int sum(int a, int b)
    {
        return a + b;
    }
}