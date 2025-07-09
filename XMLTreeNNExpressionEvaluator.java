import components.naturalnumber.NaturalNumber;
import components.naturalnumber.NaturalNumber2;
import components.simplereader.SimpleReader;
import components.simplereader.SimpleReader1L;
import components.simplewriter.SimpleWriter;
import components.simplewriter.SimpleWriter1L;
import components.utilities.Reporter;
import components.xmltree.XMLTree;
import components.xmltree.XMLTree1;

/**
 * Program to evaluate XMLTree expressions of {@code NaturalNUmber}.
 *
 * @author Syan Raval
 *
 */
public final class XMLTreeNNExpressionEvaluator {

    /**
     * Private constructor so this utility class cannot be instantiated.
     */
    private XMLTreeNNExpressionEvaluator() {
    }

    /**
     * Evaluate the given expression.
     *
     * @param exp
     *            the {@code XMLTree} representing the expression
     *
     * @return the value of the expression
     * @requires <pre>
     * [exp is a subtree of a well-formed XML arithmetic expression]  and
     *  [the label of the root of exp is not "expression"]
     * </pre>
     * @ensures evaluate = [the value of the expression]
     */
    private static NaturalNumber evaluate(XMLTree exp) {
        assert exp != null : "Violation of: exp is not null";

        String root = exp.label();
        String msg = "Divide by 0 error!";
        NaturalNumber value = new NaturalNumber2();
        if (!root.equals("number")) {
            XMLTree sub1 = exp.child(0);
            XMLTree sub2 = exp.child(1);
            if (root.equals("plus")) {
                if (sub1.hasAttribute("value")) {
                    NaturalNumber num = new NaturalNumber2(
                            Integer.parseInt(sub1.attributeValue("value")));
                    value.add(num);
                    value.add(evaluate(sub2));
                } else {
                    value.add(evaluate(sub1));
                    value.add(evaluate(sub2));
                }
            }
            if (root.equals("minus")) {
                if (sub1.hasAttribute("value")) {
                    NaturalNumber num = new NaturalNumber2(
                            Integer.parseInt(sub1.attributeValue("value")));
                    value.add(num);
                    value.subtract(evaluate(sub2));
                } else {
                    value.add(evaluate(sub1));
                    value.subtract(evaluate(sub2));
                }
            }
            if (root.equals("times")) {
                if (sub1.hasAttribute("value")) {
                    NaturalNumber num = new NaturalNumber2(
                            Integer.parseInt(sub1.attributeValue("value")));
                    value.add(num);
                    value.multiply(evaluate(sub2));
                } else {
                    value.add(evaluate(sub1));
                    value.multiply(evaluate(sub2));
                }
            }
            if (root.equals("divide")) {
                if (sub1.hasAttribute("value")) {
                    NaturalNumber num = new NaturalNumber2(
                            Integer.parseInt(sub1.attributeValue("value")));
                    value.add(num);
                    if (!evaluate(sub2).isZero()) {
                        value.divide(evaluate(sub2));
                    } else {
                        Reporter.fatalErrorToConsole(msg);
                    }

                } else {
                    value.add(evaluate(sub1));
                    if (!evaluate(sub2).isZero()) {
                        value.divide(evaluate(sub2));
                    } else {
                        Reporter.fatalErrorToConsole(msg);
                    }
                }
            }
        } else {
            NaturalNumber oneValue = new NaturalNumber2(
                    Integer.parseInt(exp.attributeValue("value")));
            value.add(oneValue);
        }

        return value;
    }

    /**
     * Main method.
     *
     * @param args
     *            the command line arguments
     */
    public static void main(String[] args) {
        SimpleReader in = new SimpleReader1L();
        SimpleWriter out = new SimpleWriter1L();

        out.print("Enter the name of an expression XML file: ");
        String file = in.nextLine();
        while (!file.equals("")) {
            XMLTree exp = new XMLTree1(file);
            out.println(evaluate(exp.child(0)));
            out.print("Enter the name of an expression XML file: ");
            file = in.nextLine();
        }

        in.close();
        out.close();
    }

}
