
import { useRouter } from 'next/router';
import { useState, useEffect } from 'react';
import { supabase } from '../../utils/supabaseClient';
import CreditCardForm from '../../components/CreditCardForm';

interface CreditCard {
  id: number;
  user_id: number;
  card_name: string;
  card_holder: string;
  ending_number?: string;
  bank_provider?: string;
  welcome_bonus: string;
  welcome_spending_amount: number;
  welcome_spending_deadline: string;
  notes?: string;
  open_date?: string;
  approved_date?: string;
}

const EditCreditCardPage: React.FC = () => {
  const router = useRouter();
  const { id } = router.query;
  const [card, setCard] = useState<CreditCard>();
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchCard = async () => {
      if (typeof id !== 'string') return;
      try {
        const { data, error } = await supabase
          .from('credit_cards')
          .select('*')
          .eq('id', id)
          .single();

        if (error) {
          console.error('Error fetching credit card:', error);
          setError('Failed to fetch credit card. Please try again later.');
        } else {
          setCard(data);
        }
      } catch (error) {
        console.error('Error fetching credit card:', error);
        setError('An unexpected error occurred.');
      } finally {
        setLoading(false);
      }
    };
    fetchCard();
  }, [id]);

  if (loading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div className="text-red-500">{error}</div>;
  }

  return (
    <div>
      {card && <CreditCardForm card={card} />}
    </div>
  );
};

export default EditCreditCardPage;