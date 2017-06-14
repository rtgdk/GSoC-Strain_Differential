import java.io.*;
import java.util.*;
import java.text.*;

class writeTest
{
	static BufferedReader br = null;
	static int finalCount = 0;
	public static void main(String[] args)
	{
		csvReader();
	}
	public static void csvReader()
	{
		String csvFile = "C:\\Users\\arpit\\Documents\\GitHub\\GSoC-Strain_Diffrential\\test scripts\\data.log";
		String line = "";		

		try
		{
			br = new BufferedReader(new FileReader(csvFile));
			int counter1 = 0;
			int counter2 = 0;
			int counter3 = 0;
			int counter4 = 0;
			int counter5 = 0;
			while((line=br.readLine()) != null)
			{
				if (line.length() > 0){
					if(line.charAt(0) == 'C' && line.length()<2)
						counter++
					// if(line.charAt(0) == '1')
					// 	counter1++;
					// if(line.charAt(0) == '2')
					// 	counter2++;
					// if(line.charAt(0) == '3')
					// 	counter3++;
					// if(line.charAt(0) == '4')
					// 	counter4++;
					// if(line.charAt(0) == '5')
					// 	counter5++;
					else
					{
						if(counter>finalCount)
							finalCount = counter;
						counter = 0;
					}
				} 	
			}
			System.out.print("\n" + finalCount);
			// System.out.print("\n" + counter1 + "\n" + counter2 +"\n" + counter3 +"\n" + counter4 +"\n" + counter5);
		}
		catch (FileNotFoundException e) 
		{
			e.printStackTrace();
		} 
		catch (IOException e) 
		{
			e.printStackTrace();
		} 
		finally 
		{
			if (br != null) {
				try 
				{
					br.close();
				} 
				catch (IOException e) 
				{
					e.printStackTrace();
				}
			}
		}
	}
}