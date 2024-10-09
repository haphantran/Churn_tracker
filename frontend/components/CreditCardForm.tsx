"use client";
import { useState, useEffect } from 'react';
import { useRouter } from 'next/navigation';
import { supabase } from '../utils/supabaseClient';
import { API_BASE_URL } from '../utils/constants';

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

interface Props {
  card?: CreditCard;
}

const CreditCardForm: React.FC<Props> = ({ card }) => {
  const router = useRouter();
  const [formData, setFormData] = useState<CreditCard>({
    id: card?.id || 0,
    user_id: card?.user_id || 0,
    card_name: card?.card_name || '',
    card_holder: card?.card_holder || '',
    ending_number: card?.ending_number || '',
    bank_provider: card?.bank_provider || '',
    welcome_bonus: card?.welcome_bonus || '',
    welcome_spending_amount: card?.welcome_spending_amount || 0,
    welcome_spending_deadline: card?.welcome_spending_deadline || '',
    notes: card?.notes || '',
    open_date: card?.open_date || '',
    approved_date: card?.approved_date || '',
  });
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const isEditing = !!card;

  useEffect(() => {
    if (isEditing) {
      setFormData(card);
    }
  }, [card, isEditing]);

  const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = event.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    setIsSubmitting(true);
    setError(null);

    try {
      const { data: { session } } = await supabase.auth.getSession();
      if (!session) {
        throw new Error('User not logged in');
      }
      const accessToken = session.access_token;

      const url = isEditing
        ? `<span class="math-inline">\{API\_BASE\_URL\}/credit\_cards/</span>{card?.id}`
        : `${API_BASE_URL}/credit_cards/`;
      const method = isEditing ? 'PUT' : 'POST';

      const response = await fetch(url, {
        method,
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${accessToken}`,
        },
        body: JSON.stringify(formData),
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.detail || 'Failed to save credit card');
      }

      router.push('/credit-cards');
    } catch (error) {
      console.error('Error saving credit card:', error);
      setError('Failed to save credit card. Please try again.');
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4"> {/* Add form container class */}
      <div className="mb-4"> {/* Add margin-bottom to each field */}
        <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="card_name">
          Card Name:
        </label>
        <input
          className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700   
 leading-tight focus:outline-none focus:shadow-outline"
          id="card_name"
          type="text"
          placeholder="Enter card name"
          name="card_name"
          value={formData.card_name}
          onChange={handleChange}
        />
      </div>
      <div className="mb-4">
        <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="card_holder">
          Card Holder:
        </label>
        <input
          className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
          id="card_holder"
          type="text"
          placeholder="Enter card holder name"
          name="card_holder"
          value={formData.card_holder}
          onChange={handleChange}
        />
      </div>
      <div className="mb-4">
        <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="bank_provider">
          Bank Provider:
        </label>
        <input
          className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
          id="bank_provider"
          type="text"
          placeholder="Enter bank provider"
          name="bank_provider"
          value={formData.bank_provider}
          onChange={handleChange}
        />
      </div>
      <div className="mb-4">
        <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="welcome_bonus">
          Welcome Bonus:
        </label>
        <input
          className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
          id="welcome_bonus"
          type="text"
          placeholder="Enter welcome bonus"
          name="welcome_bonus"
          value={formData.welcome_bonus}
          onChange={handleChange}
        />
          </div>
          <div className="mb-4">
        <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="welcome_spending_amount">
          Welcome Spending Amount:
        </label>
        <input
          className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
          id="welcome_spending_amount"
          type="number"  
          placeholder="Enter welcome spending amount"
          name="welcome_spending_amount"
          value={formData.welcome_spending_amount}
          onChange={handleChange}
        />
      </div>
      <div className="mb-4">
        <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="welcome_spending_deadline">
          Welcome Spending Deadline:
        </label>
        <input
          className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
          id="welcome_spending_deadline"
          type="date" 
          name="welcome_spending_deadline"
          value={formData.welcome_spending_deadline}
          onChange={handleChange}
        />
      </div>

      <div className="flex items-center justify-between"> {/* Add button container class */}
        <button
          className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
          type="submit"
          disabled={isSubmitting}   

        >
          {isEditing ? 'Update Credit Card' : 'Add Credit Card'}
        </button>
      </div>
      {error && <p className="text-red-500 text-xs italic mt-2">{error}</p>} {/* Add error message class */}
    </form>
  );
};

export default CreditCardForm;