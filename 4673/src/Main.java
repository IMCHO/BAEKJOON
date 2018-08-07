import java.util.ArrayList;
import java.util.List;
import java.util.Vector;

public class Main {
	static Vector<Integer> arr;
	
	public static void main(String[] args) {
		arr=new Vector<>();
		
		for(int i=1;i<=10000;i++) {
			arr.add(i);
		}
		
		//CheckSelf(arr.get(0));
		
		while(true) {
			int count=0;
			CheckSelf(arr.get(count));
			count++;
			if(count>=arr.size()) break;
		}
		
		for(int i=0;i<arr.size();i++) {
			System.out.println(arr.get(i));
		}
	}
	
	public static void CheckSelf(int num) {
		int num1=num%10;
		int num2=num/10%10;
		int num3=num/100%10;
		int num4=num/1000%10;
		int num5=num/10000%10;
		
		int remove=num+num1+num2+num3+num4+num5;
		
		//System.out.println(remove);
		if(arr.indexOf(remove)!=-1) {
			arr.remove(arr.indexOf(remove));
			CheckSelf(remove);	
		}

		//System.out.println(arr.get(1));

	}
}
